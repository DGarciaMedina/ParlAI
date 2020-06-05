import parlai.scripts.safe_interactive as safe_interactive


pp = safe_interactive.setup_args()
opt1 = pp.parse_args(
  ["-mf", "zoo:blender/blender_90M/model", "-t", "blended_skill_talk"], print_args=False
)
opt2 = pp.parse_args(
  ["-mf", "zoo:blender/blender_3B/model", "-t", "blended_skill_talk"], print_args=False
)
opt3 = pp.parse_args(
  ["-mf", "zoo:blender/blender_9B/model", "-t", "blended_skill_talk"], print_args=False
)
# opt4 = pp.parse_args(
#   ["-mf", "zoo:convai2/seq2seq/convai2_self_seq2seq_model", "-m", "legacy:seq2seq:0"], print_args=False
# )

safe_interactive.safe_interactive2([opt1])