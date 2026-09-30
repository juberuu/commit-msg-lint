import unittest

import commit_msg_lint


class LintTests(unittest.TestCase):
    def test_empty_subject(self) -> None:
        self.assertTrue(commit_msg_lint.lint(""))

    def test_valid_conventional_message(self) -> None:
        self.assertEqual(commit_msg_lint.lint("feat: add subject length check"), [])

    def test_unknown_type(self) -> None:
        errors = commit_msg_lint.lint("woo: dance")
        self.assertTrue(any("Unknown type" in error for error in errors))

    def test_long_subject(self) -> None:
        subject = "feat: " + ("x" * 80)
        errors = commit_msg_lint.lint(subject)
        self.assertTrue(any("characters" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
