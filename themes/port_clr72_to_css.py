
import sys
import argparse

p = argparse.ArgumentParser()
p.add_argument("-i", "--input", type=str, required=True, help="Input .clr file")
propmap = [
    None,                                                   # [DISASM]
    None,                                                   # 000000   //
    "CustomIDAMemo::qproperty-line-fg-default", # aaaaaa   //Default color
    "CustomIDAMemo::qproperty-line-fg-regular-comment", # f3c5ff   //Regular comment
    "CustomIDAMemo::qproperty-line-fg-repeatable-comment", # 7e6082   //Repeatable comment
    "CustomIDAMemo::qproperty-line-fg-automatic-comment", # 666666   //Automatic comment
    "CustomIDAMemo::qproperty-line-fg-insn", # ffffff   //Instruction
    "CustomIDAMemo::qproperty-line-fg-dummy-data-name", # b9ebeb   //Dummy Data Name
    "CustomIDAMemo::qproperty-line-fg-regular-data-name", # b9ebeb   //Regular Data Name
    "CustomIDAMemo::qproperty-line-fg-demangled-name", # bbecff   //Demangled Name
    "CustomIDAMemo::qproperty-line-fg-punctuation", # c0c0c0   //Punctuation
    "CustomIDAMemo::qproperty-line-fg-charlit-in-insn", # 00d269   //Char constant in instruction
    "CustomIDAMemo::qproperty-line-fg-strlit-in-insn", # 00ff00   //String constant in instruction
    "CustomIDAMemo::qproperty-line-fg-numlit-in-insn", # 3250d2   //Numeric constant in instruction
    "CustomIDAMemo::qproperty-line-fg-void-opnd", # 4646ff   //Void operand
    "CustomIDAMemo::qproperty-line-fg-code-xref", # 7faaff   //Code reference
    "CustomIDAMemo::qproperty-line-fg-data-xref", # 617c7c   //Data reference
    "CustomIDAMemo::qproperty-line-fg-code-xref-to-tail", # 3250d2   //Code reference to tail byte
    "CustomIDAMemo::qproperty-line-fg-data-xref-to-tail", # 008080   //Data reference to tail byte
    "CustomIDAMemo::qproperty-line-fg-error", # 3734ff   //Error or problem
    "CustomIDAMemo::qproperty-line-fg-line-prefix", # c0c0c0   //Line prefix
    "CustomIDAMemo::qproperty-line-fg-opcode-byte", # 595959   //Binary line prefix bytes
    "CustomIDAMemo::qproperty-line-fg-extra-line", # f3c5ff   //Extra line
    "CustomIDAMemo::qproperty-line-fg-alt-opnd", # ffaaff   //Alternative operand
    "CustomIDAMemo::qproperty-line-fg-hidden", # 00d2ff   //Hidden name
    "CustomIDAMemo::qproperty-line-fg-libfunc", # ffff00   //Library function name
    "CustomIDAMemo::qproperty-line-fg-locvar", # 0080ff   //Local variable name
    "CustomIDAMemo::qproperty-line-fg-dummy-code-name", # 00d2ff   //Dummy code name
    "CustomIDAMemo::qproperty-line-fg-asm-directive", # 00d69d   //Assembler directive
    "CustomIDAMemo::qproperty-line-fg-macro", # 7e07df   //Macro
    "CustomIDAMemo::qproperty-line-fg-strlit-in-data", # 00d269   //String constant in data directive
    "CustomIDAMemo::qproperty-line-fg-charlit-in-data", # 00f379   //Char constant in data directive
    "CustomIDAMemo::qproperty-line-fg-numlit-in-data", # 3250d2   //Numeric constant in data directive
    "CustomIDAMemo::qproperty-line-fg-keyword", # ababab   //Keywords
    "CustomIDAMemo::qproperty-line-fg-register-name", # adad73   //Register name
    "CustomIDAMemo::qproperty-line-fg-import-name", # fd5aff   //Imported name
    "CustomIDAMemo::qproperty-line-fg-segment-name", # 7fffff   //Segment name
    "CustomIDAMemo::qproperty-line-fg-dummy-unknown-name", # 00ffaa   //Dummy unknown name
    "CustomIDAMemo::qproperty-line-fg-code-name", # 00d2ff   //Regular code name
    "CustomIDAMemo::qproperty-line-fg-unknown-name", # ffaaff   //Regular unknown name
    "CustomIDAMemo::qproperty-line-fg-collapsed-line", # 00ffff   //Collapsed line
    None, # 000000   //Max color number
    # STARTING HERE, EVERYTHING GOES SIDEWAYS
    "CustomIDAMemo::qproperty-line-bg-default", # 2d2d2d
    "CustomIDAMemo::qproperty-line-bg-selected", # 32ade1
    "CustomIDAMemo::qproperty-line-pfx-libfunc", # ffff00
    "CustomIDAMemo::qproperty-line-pfx-func", # 666666
    "CustomIDAMemo::qproperty-line-pfx-insn", # 0000aa
    "CustomIDAMemo::qproperty-line-pfx-data", # 617c7c
    "CustomIDAMemo::qproperty-line-pfx-unexplored", # 009d9d
    "CustomIDAMemo::qproperty-line-pfx-extern", # ff55ff
    "CustomIDAMemo::qproperty-line-pfx-current-item", # 000000
    "CustomIDAMemo::qproperty-line-pfx-current-line", # 00aaff
    None, # 000000
    "CustomIDAMemo::qproperty-line-pfx-lumina", # 32cd32
    None, # [NAVBAR]
    "navband_t::qproperty-lib-function", # ffaa00   //Library function
    "navband_t::qproperty-function", # 00aaff   //Regular function
    "navband_t::qproperty-code", # 000080   //Instruction
    "navband_t::qproperty-data", # b9ebeb   //Data item
    "navband_t::qproperty-undefined", # 007878   //Unexplored
    "navband_t::qproperty-extern", # ff00ff   //External symbol
    "navband_t::qproperty-error", # 0000ca   //Errors
    "navband_t::qproperty-gap", # 4a4a4a   //Gaps
    "navband_t::qproperty-cursor", # 00ff80   //Cursor
    "navband_t::qproperty-auto-analysis-cursor", # 0080ff   //Address
    "navband_t::qproperty-lumina-function", # 0080ff   //Lumina function
    None, # [DEBUG]
    "CustomIDAMemo::qproperty-line-bg-dbg-ip", # ffd060   //Current IP
    "CustomIDAMemo::qproperty-line-bg-dbg-ip-bpt-enabled", # ffa0a0   //Current IP (+ enabled breakpoint)
    "CustomIDAMemo::qproperty-line-bg-dbg-ip-bpt-disabled", # 408020   //Current IP (+ disabled breakpoint)
    "CustomIDAMemo::qproperty-line-bg-dbg", # ffffcc   //Default background
    "CustomIDAMemo::qproperty-line-bg-dbg-bpt-enabled", # 000076   //Address (+ enabled breakpoint)
    "CustomIDAMemo::qproperty-line-bg-dbg-bpt-disabled", # 00ff00   //Address (+ disabled breakpoint)
    "CustomIDAMemo::qproperty-line-bg-dbg-ip-bpt-unavailable", # 004080   //Current IP (+ unavailable breakpoint)
    "CustomIDAMemo::qproperty-line-bg-dbg-bpt-unavailable", # 0080ff   //Address (+ unavailable breakpoint)
    "TCpuRegs::qproperty-register-defined", # 000000   //Registers
    "TCpuRegs::qproperty-register-changed", # ff0000   //Registers (changed)
    "TCpuRegs::qproperty-register-edited", # 800080   //Registers (edited)
    "TCpuRegs::qproperty-register-unavailable", # 808080   //Registers (unavailable)
    None, # [ARROW]
    "TextArrows::qproperty-jump-in-function", # 34466c   //Jump in current function
    "TextArrows::qproperty-jump-external-to-function", # dede00   //Jump external to function
    "TextArrows::qproperty-jump-under-cursor", # 00aaff   //Jump under the cursor
    "TextArrows::qproperty-jump-target", # 008000   //Jump target
    "TextArrows::qproperty-register-target", # ff4040   //Register target
    None, # [GRAPH]
    "CustomIDAMemo::qproperty-graph-bg-top", # b2b2b2   //Top color
    "CustomIDAMemo::qproperty-graph-bg-bottom", # b2b2b2   //Bottom color
    "CustomIDAMemo::qproperty-graph-node-title-normal", # f5f5f5   //Normal title
    "CustomIDAMemo::qproperty-graph-node-title-selected", # 989faa   //Selected title
    "CustomIDAMemo::qproperty-graph-node-title-current", # 54585e   //Current title
    "CustomIDAMemo::qproperty-graph-node-frame-group", # 00ffff   //Group frame
    "CustomIDAMemo::qproperty-graph-node-shadow", # 242424   //Node shadow
    "CustomIDAMemo::qproperty-graph-node-high1", # 003900   //Highlight color 1
    "CustomIDAMemo::qproperty-graph-node-high2", # 00006d   //Highlight color 2
    "CustomIDAMemo::qproperty-graph-node-foreign", # 0000ff   //Foreign node
    "CustomIDAMemo::qproperty-graph-edge-normal", # cb4300   //Normal edge
    "CustomIDAMemo::qproperty-graph-edge-yes", # 009100   //Yes edge
    "CustomIDAMemo::qproperty-graph-edge-no", # 0000bc   //No edge
    "CustomIDAMemo::qproperty-graph-edge-high", # ffaaaa   //Highlighted edge
    "CustomIDAMemo::qproperty-graph-edge-current", # 008ec6   //Current edge
    None, # [MISC]
    "MainMsgList::color", # 212121   //Message text
    "MainMsgList::background-color", # d4d4d4   //Message background
    "CustomIDAMemo::qproperty-line-fg-patched-bytes", # 404080   //Patched bytes
    "CustomIDAMemo::qproperty-line-fg-unsaved-changes", # 0080ff   //Unsaved changes
    None, # [OTHER]
    "CustomIDAMemo::qproperty-line-bg-highlight", # 00ffff   //Highlight color
    "CustomIDAMemo::qproperty-line-bg-hint", # e1ffff   //Hint color
    None, # [SYNTAX]
    # "", # ff0000  0  0   //Keyword 1
    # "", # 800080  0  0   //Keyword 2
    # "", # 0000ff  0  0   //Keyword 3
    # "", # 00008b  0  0   //String
    # "", # 006400  0  1   //Comment
    # "", # ff0000  1  0   //Preprocessor
    # "", # 8b8b00  1  0   //Number
]

args = p.parse_args()
with open(args.input) as fin:
    lines = fin.readlines()
lines = map(str.rstrip, lines)

css = {
    "CustomIDAMemo" : [],
    "TextArrows" : [],
    "MainMsgList" : [],
    "TCpuRegs" : [],
    "navband_t" : [],
}

ignorable = [
    "",
    "Max color number",
]

for idx, line in enumerate(lines):
    if idx >= len(propmap):
        break
    prop = propmap[idx]
    if prop is not None:
        parts = line.split()
        color = parts[0].strip()
        try:
            color = int(color, 16)
        except:
            sys.stderr.write("warning: couldn't turn \"%s\" into an integer; skipping\n" % color)
            continue
        type_name, prop_name = tuple(prop.split("::"))
        css[type_name].append((prop_name, color))

for type_name in sorted(css.keys()):
    data = css[type_name]
    if data:
        print("%s" % type_name)
        print("{")
        for prop, color in data:
            print("    %s: #%02x%02x%02x;" % (
                prop,
                color & 0xff,
                (color >> 8) & 0xff,
                (color >> 16) & 0xff))
        print("}")
