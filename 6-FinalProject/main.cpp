#include "BrainFuckInterpreter.hpp"
#include "CommandLineParser.hpp"

const static char *BF_INTERPRETER_VERSION = "1.0.2";
const static char *COMPILER =
#ifdef __clang__
        "clang++";
#elif __GNUC__
"g++";
#elif _MSC_VER
"MSVC";
#else
"Unknown Compiler";
#warning "Unknown Compiler detected"
#endif
const static char *RIGHTS = "Mux BrainFuck Interpreter, CopyRight: Mux 2022";
const static char *HELLO_WORLD_EXAMPLE =
        "# This is a comment~\n"
        "++++++++++\n"
        "[\n\t>+++++++>++++++++++>+++>+<<<<-\n]\n"
        ">++.>+.+++++++..+++.>++.<<+++++++++++++++.\n"
        ">.+++.------.--------.>+.>.\n"
        "# To see and clean the runtime-stack.\n"
        "[%[-]<]";
const static size_t CPP_STD_VERSION = __cplusplus / 10000;
const static char *HELP_DOC =
        "bf [-f: file_path] [-s: stack size] [-h/--help/-help: document] [-v/--version/-version: version]\n"
        "[--hello_world: to see the hello world program example.]"
        "Mux Version brain fuck Syntax: \n"
        "'+': Increase byte at the data pointer by one.\n"
        "'-': Decrease byte at the data pointer by one.\n"
        "'<': Move the data pointer to point to the next cell to the left.\n"
        "'>': Move the data pointer to point to the next cell to the right.\n"
        "']': Jump to the next instruction of the matching [, "
        "if the data pointed to by the current data pointer is not 0\n"
        "'.': Output the byte at the data pointer.\n"
        "',': Accept one byte of input, storing its value in the byte at the data pointer.\n"
        "'#': Comment\n"
        "';': Display the entire run stack\n"
        "':': Display the current position of the data pointer\n"
        "'%': Display the contents of the runtime stack from the start to the data pointer position\n"
        "'&': Pause Program until user press any key.";
int main(int argc, char *argv[]) {
    CommandLineParser parser(argc, argv);

    if (argc == 1) {
        cout << "use brainfuck --help to see how to use." << endl;
        return 0;
    }
    if (parser.cmd_option_exists("-h") ||
        parser.cmd_option_exists("--help") ||
        parser.cmd_option_exists("-help")) {
        cout << HELP_DOC << endl;
        return 0;
    }
    if (parser.cmd_option_exists("-v") || parser.cmd_option_exists("--version") ||
        parser.cmd_option_exists("-version")) {
        cout << RIGHTS << "\n[Compiler and C++ Version used to build BrainFuck: " << COMPILER << "/std:"
             << CPP_STD_VERSION
             << ']'
             << endl;
        cout << "Version: " << BF_INTERPRETER_VERSION << endl;

        return 0;
    }

    if (parser.cmd_option_exists("--hello_world")) {
        cout << "Copy and paste the content below to a file, and use command: \n"
                "bf -f <file_name>\n"
                "to run hello world program\n";
        cout << HELLO_WORLD_EXAMPLE << endl;
        return 0;
    }
    string path = parser.cmd_option_exists("-f") ? parser.get_cmd_option("-f") : "";
    if (path.empty()) {
        cerr << "File path is empty." << endl;
        cerr << "Use option -f to tell interpreter where is the script file." << endl;
        cerr << "example: BrainFuck -f test.bf" << endl;
        return 0;
    }
    int stack_size = [&parser]() -> int {
        if (parser.cmd_option_exists("-s")) {
            stringstream ss(parser.get_cmd_option("-s"));
            int ret;
            ss >> ret;
            return ret;
        } else
            return 300;
    }();
    return Interpreter()(path, stack_size);
}
