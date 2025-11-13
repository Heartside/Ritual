from muxtools import (
    GlobSearch,
    Premux,
    Setup,
    SubFile,
    mux,
    ASSHeader,
)

setup = Setup(
    "01",
    None,
    out_dir="out",
    mkv_title_naming="",
    out_name=R"Ritual (2000) - S01E$ep$ (BD 1080p x264 Opus) [$crc32$] [Heartside]",
    clean_work_dirs=True,
    error_on_danger=True,
)

premux = GlobSearch("./Ritual - Premux*.mkv")

premux = Premux(
    premux,
    subtitles=None,
    keep_attachments=False,
    mkvmerge_args="--no-global-tags --title 'Ritual (2000)' --track-name 0:'2016 JPBD [Anonymous]' --language 0:und --default-track-flag 0:1 --track-name 1:'Opus 5.0 @ 320kb/s [JPBD]' --language 1:jpn --default-track-flag 1:1 --original-flag 1:1",
)

dialogue = SubFile("./Ritual - Dialogue.ass")

dialogue = dialogue.set_headers(
    (ASSHeader.PlayResX, 1920),
    (ASSHeader.PlayResY, 1080),
    (ASSHeader.LayoutResX, 1920),
    (ASSHeader.LayoutResY, 1080),
    (ASSHeader.YCbCr_Matrix, "TV.709"),
    (ASSHeader.ScaledBorderAndShadow, True),
    (ASSHeader.WrapStyle, 0),
)

dialogue = dialogue.clean_comments().clean_extradata().clean_garbage().clean_styles()

fonts = dialogue.collect_fonts(use_system_fonts=False)

mux(
    premux,
    dialogue.to_track("Full Subtitles [Heartside]", "eng", default=True, forced=False),
    *fonts,
)
