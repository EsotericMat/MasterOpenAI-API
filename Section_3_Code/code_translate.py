from code_assistance import CodeAssitance
CA = CodeAssitance()

js = """
func mystery: {
    for (var i = 1; i < 101; i++) {
        if (i % 15 == 0) console.log("Mys");
        else if (i % 3 == 0) console.log("Tery");
        else if (i % 5 == 0) console.log("Mystery");
        else console.log(i);
        }
    }
"""

CA.translate(
    'Javascript', 'Python', js
)
