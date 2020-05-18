use std::io;
use std::io::{BufReader, BufRead};

fn main() {
    let mut reader = BufReader::new(io::stdin());
    let mut buffer: String = String::new();
    reader.read_line(&mut buffer).expect("Failed read line");

    let mut buffer: String = String::new();
    reader.read_line(&mut buffer).expect("Failed to read array");
    let mut array: Vec<u8> = Vec::new();
    for number in buffer.split_whitespace() {
        array.push(number.parse::<u8>().expect("Fail to parse u8"))
    }
    let str_arr: Vec<String> = count_sort(array).iter().map(|x| x.to_string()).collect();
    println!("{}", str_arr.join(" "))
}

fn count_sort(array: Vec<u8>) -> Vec<u8> {
    let mut counter: Vec<u16> = vec![0;11];
    for elem in array.iter() {
        counter[*elem as usize] += 1;
    }

    let mut positions: Vec<u16> = counter.iter().scan(0, |acc, x| {
        *acc += x;
        Some(*acc)
    }).collect();

    let mut sorted: Vec<u8> = vec![0;array.len()];
    for elem in array {
        let pos = positions[elem as usize];
        let index = positions.get_mut(elem as usize).expect("Cannot get value");

        *index -= 1;
        sorted[(pos - 1) as usize] = elem;
    }
    sorted
}
