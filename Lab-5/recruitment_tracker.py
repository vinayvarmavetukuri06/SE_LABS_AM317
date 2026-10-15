"""Applicant tracking system using an SQLite database."""

import csv
import sqlite3

conn = sqlite3.connect(":memory:")

conn.execute(
    """
    CREATE TABLE applicants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        role TEXT,
        expected_salary INTEGER,
        status TEXT
    )
    """
)


def add_applicant(
    name: str,
    role: str,
    expected_salary: int,
    status: str = "applied",
) -> None:
    """Add an applicant to the database."""
    conn.execute(
        """
        INSERT INTO applicants (
            name, role, expected_salary, status
        )
        VALUES (?, ?, ?, ?)
        """,
        (name, role, expected_salary, status),
    )
    conn.commit()


def shortlist(role: str, salary_limit: int) -> list[str]:
    """Return applicants whose salary expectations fit the limit."""
    rows = conn.execute(
        """
        SELECT name, expected_salary
        FROM applicants
        WHERE role = ?
        """,
        (role,),
    ).fetchall()

    return [
        name
        for name, salary in rows
        if salary <= salary_limit
    ]


def update_status(applicant_id: int, status: str) -> None:
    """Update an applicant's hiring status."""
    conn.execute(
        """
        UPDATE applicants
        SET status = ?
        WHERE id = ?
        """,
        (status, applicant_id),
    )
    conn.commit()


def export_report(path: str) -> None:
    """Export applicant names, roles, and statuses to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as report_file:
        writer = csv.writer(report_file)
        writer.writerows(
            conn.execute(
                "SELECT name, role, status FROM applicants"
            )
        )


def count_by_status(status: str) -> int:
    """Return the number of applicants with the given status."""
    result = conn.execute(
        "SELECT COUNT(*) FROM applicants WHERE status = ?",
        (status,),
    ).fetchone()

    return result[0]


def main() -> None:
    """Run the applicant tracking system demonstration."""
    add_applicant("Nina", "analyst", 600000)
    add_applicant("Omar", "analyst", 750000, "interview")
    add_applicant("Priya", "developer", 900000)

    update_status(1, "interview")

    print(shortlist("analyst", 500000 + 150000))

    export_report("applicants_report.csv")

    print(count_by_status("interview"), "in interview")


if __name__ == "__main__":
    main()
