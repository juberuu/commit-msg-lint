# commit-msg-lint

A small Python checker for commit messages. It currently verifies that the subject line is present and not empty.

## Usage

```bash
python commit_msg_lint.py ".git/COMMIT_EDITMSG"
```

Or pipe a message:

```bash
echo "Add directory ignore rules" | python commit_msg_lint.py
```
