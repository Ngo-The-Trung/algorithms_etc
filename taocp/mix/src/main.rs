use std::io::{self, BufRead, BufReader};
use std::fs::File;
// use std::env::args;


const MEM_MAX: usize = 4000;
const BYTE_SIZE: usize = 64;
const BYTE_MAX: i32 = 64;

struct MixByte {
    val: u8,
}

enum MixSign {
    Positive = 1,
    Negative = -1,
}

struct MixWord {
    sign: MixSign,
    bytes: [MixByte; 5],
}

struct MixSmallWord {
    sign: MixSign,
    bytes: [MixByte; 2],
}

struct MixRegisters {
    A: MixWord,
    X: MixWord,
    I: [MixSmallWord; 6],
    J: MixSmallWord,
}

enum MixOverflow {
    On,
    Off,
}

enum MixComparison {
    LESS,
    EQUAL,
    GREATER,
}

struct Flags {
    overflow: MixOverflow,
    cmp: MixComparison,
}

enum MixOpCode {
    NOP,
    ADD,
    SUB,
    MUL,
    DIV,
    CHAR,
}

struct Instruction {
    opcode: MixOpCode,
    address: i32,
    index: u8,
    modifier: u8,
}

impl Instruction {
    fn from_word(w: MixWord) {
        let addr: i32 = (w.sign as i32) * (w.bytes[0].val as i32) * BYTE_MAX +
                        (w.bytes[1].val as i32);
        let index = w.bytes[2];
        let modifier = w.bytes[3];
    }
}

struct MixMachine {
    regs: MixRegisters,
    mem: [MixByte; MEM_MAX],
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        println!("Usage: mix <filename>");
        std::process::exit(1);
    } else {
        let file = File::open(&args[1]).unwrap();
        let mut reader = BufReader::new(file);
        let mut line = String::new();
        while let Ok(len) = reader.read_line(&mut line) {
            if len > 0 {
                print!("{}", line);
                line.clear();
            } else {
                break;
            }
        }
    }
}
