use std::fs;
use std::cmp::max;
use std::convert::TryInto;

fn main() {
    let filename = "C:\\Users\\Steve\\Desktop\\Advent Of Code\\input\\Day19.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    
    // println!("{}", contents);
    let summands = contents.split('\n');
}
