def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": f"{error['code']} {error['text']}",
        "type": "error" if error["code"].startswith("E") else "warning"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        file_path: [format_linter_error(single_error) for single_error in errors]
    }


def format_linter_report(linter_report: dict) -> list:
    all_errors = []
    for file_errors in linter_report.values():
        for error in file_errors:
            all_errors.append(format_linter_error(error))
    return all_errors
