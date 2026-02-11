def calculate_confidence(report_count):
    if report_count >= 10:
        return "High"
    elif report_count >= 5:
        return "Medium"
    return "Low"
