from muxtools import (
    GlobSearch,
    Premux,
    Setup,
    SubFile,
    mux,
    ASSHeader,
    Chapters
)

setup = Setup(
    episode="01",
    config_file=None,
    out_dir="out",
    mkv_title_naming="",
    out_name=R"Ritual (2000) (BD 1080p x264 AC-3) [$crc32$] [Heartside]",
    clean_work_dirs=True,
    error_on_danger=True,
)

premux = GlobSearch("./Ritual - Premux*.mkv")

premux = Premux(
    premux,
    subtitles=None,
    keep_attachments=False,
    mkvmerge_args="--no-global-tags --title 'Ritual (2000)' --track-name 0:'2016 JPBD Encode [Anonymous]' --language 0:und --default-track-flag 0:1 --track-name 1:'AC-3 5.0 @ 640kb/s [JPBD]' --language 1:jpn --default-track-flag 1:1 --original-flag 1:1",
)

dialogue = SubFile("./Ritual - Dialogue.ass")

dialogue = dialogue.set_headers(
    (ASSHeader.PlayResX, 1920),
    (ASSHeader.PlayResY, 804),
    (ASSHeader.LayoutResX, 1920),
    (ASSHeader.LayoutResY, 804),
    (ASSHeader.YCbCr_Matrix, "TV.709"),
    (ASSHeader.ScaledBorderAndShadow, True),
    (ASSHeader.WrapStyle, 0),
)

dialogue = dialogue.clean_comments().clean_extradata().clean_garbage().clean_styles()

fonts = dialogue.collect_fonts(use_system_fonts=True)

chapters = Chapters("Ritual - Chapters.txt")

mux(
    premux,
    dialogue.to_track("Full Subtitles [Heartside]", "eng", default=True, forced=False),
    *fonts,
    chapters,
)
