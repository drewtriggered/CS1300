def getStatistics(data):
    total = len(data)
    if total == 0:
        return {
            'total': 0,
            'average': 0,
            'max': 0,
            'min': 0
        }
    
    average = sum(data) / total
    max_value = max(data)
    min_value = min(data)
    
    return {
        'total': total,
        'average': average,
        'max': max_value,
        'min': min_value
    }