from typing import Optional

from mistune import Markdown

from .genericblock import parse_generic_block_close, parse_generic_block_open

QUOTE_OPEN_PATTERN = r"(\s+)?\[quote(=(\"|')?([\w\-_]*)(:(\d+))?)?(\"|')?\](\s+)?"
QUOTE_CLOSE_PATTERN = r"(\s+)?\[\/quote\](\s+)?"


@parse_generic_block_open
def parse_quote_open_bbcode(parser, m, state: dict):
    author = m.group(4) or ""
    post: Optional[int] = None

    try:
        post = int((m.group(6) or "").strip())
    except (TypeError, ValueError):
        pass

    return {
        "type": "quote_bbcode",
        "author": author.strip() or None,
        "post": post if post and post > 0 else None,
    }


@parse_generic_block_close
def parse_quote_close_bbcode(parser, m, state: dict):
    return {"type": "quote_bbcode"}


def plugin_quote_bbcode(markdown: Markdown):
    markdown.inline.register_rule(
        "quote_open_bbcode", QUOTE_OPEN_PATTERN, parse_quote_open_bbcode
    )
    markdown.inline.register_rule(
        "quote_close_bbcode", QUOTE_CLOSE_PATTERN, parse_quote_close_bbcode
    )
    markdown.inline.rules.append("quote_open_bbcode")
    markdown.inline.rules.append("quote_close_bbcode")
