# commit-msg-lint

A small Python checker for commit messages. It verifies that the subject exists, stays short, and uses a conventional type when a prefix is present.

## Usage

```bash
python commit_msg_lint.py ".git/COMMIT_EDITMSG"
```

Or pipe a message:

```bash
echo "feat: add directory ignore rules" | python commit_msg_lint.py
```

## Tests

```bash
python -m unittest discover -v
```
