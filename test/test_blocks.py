from slackblocks import ContextBlock, DividerBlock, ImageBlock, SectionBlock, Text


def test_basic_section_block() -> None:
    block = SectionBlock("Hello, world!",
                         block_id="fake_block_id")
    with open("test/samples/section_block_text_only.json", "r") as expected:
        assert expected.read() == repr(block)


def test_basic_context_block() -> None:
    block = ContextBlock(elements=[Text("Hello, world!")],
                         block_id="fake_block_id")
    with open("test/samples/context_block_text_only.json", "r") as expected:
        assert expected.read() == repr(block)


def test_basic_divider_block() -> None:
    block = DividerBlock(block_id="fake_block_id")
    with open("test/samples/divider_block_only.json", "r") as expected:
        assert expected.read() == repr(block)


def test_basic_image_block() -> None:
    block = ImageBlock(image_url="https://api.slack.com/img/blocks/bkb_template_images/beagle.png",
                       alt_text="image1",
                       title="image1",
                       block_id="fake_block_id")
    with open("test/samples/image_block_only.json", "r") as expected:
        assert expected.read() == repr(block)
