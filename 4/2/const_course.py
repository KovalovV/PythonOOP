COURSES_JSON = 'C:/MinGW/bin/cpp/Python/4/2/course.json'
TEACHERS_JSON = 'C:/MinGW/bin/cpp/Python/4/2/teachers.json'

SCHEMA_COURSE = {
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "required": [
            "type",
                "theme"
        ],
        "properties": {
            "type": {"type": "string", "enum": ["local", "offsite"]},
            "theme": {"type": "array", "items": {"type": "string"}, "maxItems": 4},
        }
    }
}

SCHEMA_TEACHER = {
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "required": [
            "courses",
        ],
        "properties": {
            "courses": {"type": "string", "enum": ["local", "offsite"]},
            "courses": {"type": "array", "items": {"type": "string"}, "maxItems": 3},
        }
    }
}
