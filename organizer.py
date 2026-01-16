import base64
from pathlib import Path
from datetime import datetime, timedelta
import os
import re
import json

def encode_image(image_path: str) -> tuple[str, str]:
    """Encode image to base64 and determine media type."""
    path = Path(image_path)
    extension = path.suffix.lower()
    
    media_type_map = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp'
    }
    
    media_type = media_type_map.get(extension, 'image/jpeg')
    
    with open(image_path, 'rb') as f:
        image_data = base64.standard_b64encode(f.read()).decode('utf-8')
    
    return image_data, media_type


def convert_json_to_text(json_schedule: dict) -> str:
    """Convert JSON schedule format to text format for uniform processing."""
    text = ""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    if 'busy' in json_schedule:
        text += "busy:\n"
        for day in days:
            if day in json_schedule['busy']:
                times = json_schedule['busy'][day]
                text += f"{day}: {', '.join(times)}\n"
    
    if 'available' in json_schedule:
        text += "available:\n"
        for day in days:
            if day in json_schedule['available']:
                times = json_schedule['available'][day]
                text += f"{day}: {', '.join(times)}\n"
    
    return text


def analyze_schedules(schedules: list[dict]) -> str:
    """
    Analyze schedules from images and text to find optimal meeting time.
    
    Args:
        schedules: List of dicts with 'type' ('image', 'text', or 'json') and 'content'
    
    Returns:
        Recommended meeting time with availability analysis
    """
    def score_time_slots(schedules: list[dict]) -> dict:
        """Score each time slot based on availability."""
        slots = {}
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        hours = range(8, 22)  # 8 AM to 10 PM
        
        # Initialize all slots with score 0
        for day in days:
            for hour in hours:
                slots[f"{day} {hour}:00"] = 0
        
        # Parse and score each person's availability
        for schedule in schedules:
            if schedule['type'] == 'json':
                text = convert_json_to_text(schedule['content'])
            else:
                text = schedule['content']
            
            for day in days:
                for hour in hours:
                    if is_available_in_text(text, day, hour):
                        slots[f"{day} {hour}:00"] += 1
        
        return slots

    def is_available_in_text(text: str, day: str, hour: int) -> bool:
        """Check if person is available during given day/hour."""
        text_lower = text.lower()
        day_lower = day.lower()
        
        # Split text into lines and find the section for this day
        lines = text_lower.split('\n')
        day_start_idx = -1
        section_type = None  # 'busy' or 'available'
        
        # Find which line contains this day
        for i, line in enumerate(lines):
            if day_lower in line:
                day_start_idx = i
                # Look backwards to find if we're in a 'busy' or 'available' section
                for j in range(i, -1, -1):
                    if 'busy' in lines[j]:
                        section_type = 'busy'
                        break
                    elif 'available' in lines[j]:
                        section_type = 'available'
                        break
                break
        
        if day_start_idx == -1:
            return True  # If day not mentioned, assume available
        
        # Get the text for this specific day
        day_text = lines[day_start_idx]
        
        # Extract time ranges from this day's line (format: "9:30 AM - 10:45 AM")
        time_range_pattern = r'(\d{1,2}):?(\d{2})?\s*(am|pm)?\s*-\s*(\d{1,2}):?(\d{2})?\s*(am|pm)?'
        time_ranges = re.findall(time_range_pattern, day_text, re.IGNORECASE)
        
        if not time_ranges:
            # No specific times mentioned for this day
            if section_type == 'available':
                return False  # "Available" with no times = nothing is available
            return True  # "Busy" with no times = available (no busy hours listed)
        
        # Parse time ranges and check if hour falls within any
        hour_in_range = False
        for match in time_ranges:
            start_hour = int(match[0])
            start_min = int(match[1]) if match[1] else 0
            start_period = match[2].lower() if match[2] else 'am'
            
            end_hour = int(match[3])
            end_min = int(match[4]) if match[4] else 0
            end_period = match[5].lower() if match[5] else 'pm'
            
            # Convert to 24-hour format
            if start_period == 'pm' and start_hour != 12:
                start_hour += 12
            elif start_period == 'am' and start_hour == 12:
                start_hour = 0
            
            if end_period == 'pm' and end_hour != 12:
                end_hour += 12
            elif end_period == 'am' and end_hour == 12:
                end_hour = 0
            
            # Check if hour falls within this range
            if start_hour <= hour < end_hour:
                hour_in_range = True
                break
        
        # Apply logic based on section type
        if section_type == 'busy':
            # For busy section: listed times are busy, so return False if in range
            return not hour_in_range
        elif section_type == 'available':
            # For available section: listed times are available, so return True if in range
            return hour_in_range
        
        return True  # Default to available if no section type found

    # Score all time slots
    time_slot_scores = score_time_slots(schedules)
    
    # Display the complete scoring results for all time slots
    print("\nComplete Time Slot Scoring:")
    print("-" * 40)
    for slot in sorted(time_slot_scores.keys()):
        score = time_slot_scores[slot]
        print(f"{slot}: {score}/2 available")
    print("-" * 40)
    
    best_slot = max(time_slot_scores, key=time_slot_scores.get)
    return best_slot

def main():
    schedules = [
    {
        "type": "json",
        "content": {
            "name": "Kai",
            "busy": {
                "Monday": ["9:30 AM - 10:45 AM", "12:30 PM - 1:45 PM"],
                "Tuesday": ["11:00 AM - 3:15 PM"],
                "Wednesday": ["9:00 AM - 11:00 AM"],
                "Thursday": ["9:30 AM - 10:45 AM", "12:30 PM - 1:45 PM"],
                "Friday": ["11:00 AM - 3:15 PM", "9:00 AM - 11:00 AM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "Jordan",
            "available": {
                "Monday": ["8:00 PM - 10:00 PM"],
                "Tuesday": ["9:30 AM - 2:15 PM", "9:00 PM 10:00 PM"],
                "Wednesday": ["8:00 AM - 11:30 PM", "8:00 PM - 10:00 PM"],
                "Thursday": ["12:30 PM - 4:30 PM", "8:00 PM - 10:00 PM"],
                "Friday": ["8:00 AM - 2:30 PM", "9:00 PM - 10:00 PM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "Seth",
            "available": {
                "Monday": ["8:00 AM - 8:00 PM"],
                "Tuesday": ["8:00 AM - 1:45 PM", "3:30 PM - 10:00 PM"],
                "Wednesday": ["8:00 AM - 3:30 PM,"],
                "Thursday": ["12:30 PM - 3:30 PM", "7:15 PM - 10:00 PM"],
                "Friday": ["8:30 AM - 1:30 PM", "6:30 PM - 10:00 PM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "AJ",
            "available": {
                "Monday": ["3:00 PM - 5:00 PM"],
                "Tuesday": ["12:30 PM - 1:45 PM", "3:30 PM - 5:00 PM", "7:00 PM - 10:00 PM"],
                "Wednesday": ["1:00 PM - 4:30 PM"],
                "Thursday": ["8:00 AM - 9:00 AM", "8:30 PM - 10:00 PM"],
                "Friday": ["3:30 PM - 10:00 PM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "Ocean",
            "available": {
                "Monday": ["3:00 PM - 10:00 PM"],
                "Tuesday": ["3:30 PM - 10:00 PM"],
                "Wednesday": ["8:00 AM - 1:00 PM", "5:00 PM - 10:00 PM"],
                "Thursday": ["8:00 AM - 10:00 AM, 2:00 PM - 10:00 PM"],
                "Friday": ["3:30 PM - 10:00 PM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "Ella",
            "available": {
                "Monday": ["8:00 AM - 10:00 PM"],
                "Tuesday": ["10:00 AM - 11:00 AM", "3:30 PM - 10:00 PM"],
                "Wednesday": ["8:00 AM - 6:00 PM", "8:30 PM - 10:00 PM"],
                "Thursday": ["8:00 AM - 10:00 PM"],
                "Friday": ["10:00 AM - 11:00 AM", "3:30 PM - 10:00 PM"]
            }
        }
    },
    {
        "type": "json",
        "content": {
            "name": "Drew",
            "available": {
                "Monday": ["11:30 AM - 10:00 PM"],
                "Tuesday": ["8:00 AM - 9:00 AM, 6:30 PM- 10:00 PM"],
                "Wednesday": ["8:00 AM - 9:30 AM, 6:30 PM - 10:00 PM"],
                "Thursday": ["8:00 AM - 10:45 AM, 6:30 PM - 10:00 PM"],
                "Friday": ["8:00 AM - 9:15 AM, 6:30 PM - 10:00 PM"]
            }
        }
    }
]

    best_slot = analyze_schedules(schedules)
    print("Meeting Analysis:")
    print(best_slot)


if __name__ == "__main__":
    main()