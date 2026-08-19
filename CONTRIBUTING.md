# Contributing

This is a portfolio mirror. The active development happens in a private repo. Public contributions are limited to:

- Filing issues for factual errors in the charter, architecture, or revenue-channel docs.
- Proposing typo fixes and broken-link corrections via pull request.
- Suggesting additional documentation topics that would help external readers.

## What I will accept

- **Documentation patches.** Markdown formatting, broken links, factual corrections.
- **Citation additions.** If you spot a claim that needs a source, propose the source.
- **Translation PRs.** Turkish and German translations are welcome.

## What I will not accept

- **Code changes.** The implementation lives in a private repo. Public patches here are not the right path.
- **Strategy proposals.** Martingale, grid, recovery, average-down are refused up front. See [CHARTER.md §3](CHARTER.md).
- **New revenue channels.** The list in [CHARTER.md §5](CHARTER.md) is closed to public proposals. The operator adds channels, not the other way around.
- **AI-generated bulk PRs.** I will close them. Be a human.

## Pull request process

1. Fork the repo, branch off `main`.
2. One PR per logical change. Smaller is better.
3. Sign your commit (`git commit -s`) if you want it attributed in the contributor list.
4. Open the PR. I will review within a week.
5. PRs that touch `CHARTER.md` or `docs/HARD-CONSTRAINTS.md` require explicit justification in the PR body. These are anchor documents.

## Issue process

Open an issue with:

- A clear title.
- A specific claim or section reference.
- What you propose and why.

If the issue is a factual error, include the source. If it is a norm change, do not be surprised if it gets closed without action.

## Style

- Markdown. Tables over prose where possible.
- Direct sentence structures. No filler.
- ASCII-safe. The charter is read in terminals, terminals do not always render Unicode.
- Code blocks with language hints.

## License

By contributing, you agree your contributions are licensed under the MIT license. See [LICENSE](LICENSE).
