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
    all_errors = []
    # Важливо: ми проходимо по всіх файлах у звіті
    for path, errors in linter_report.items():
        # Для кожного файлу форматуємо його список помилок
        for e in errors:
            all_errors.append(format_linter_error(e))
    return all_errors
