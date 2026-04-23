def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": f"{error['code']} {error['text']}",
        "type": "error" if error["code"].startswith("E") else "warning"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        file_path: [format_linter_error(e) for e in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    result = []
    for path, errors in linter_report.items():
        # Ми беремо результат другої функції (словник)
        # і дістаємо з нього список відформатованих помилок
        formatted_file = format_single_linter_file(path, errors)
        result.extend(formatted_file[path])
    return result
