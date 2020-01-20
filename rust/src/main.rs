use std::io;
use std::dbg;

fn main() {

    let mut input: String = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Unable to read from 'stdin'!");

    let size: u16 = input.trim().parse().expect("Error during conversion to u16");
    dbg!(size);

    let mut ranges: Vec<(u16, u16)> = Vec::new();
    for _ in 0..size {
        input.clear();
        io::stdin()
            .read_line(&mut input)
            .expect("Unable to read range from stdin");

        let parts: Vec<&str> = input.split(' ').collect();
        let range: (u16, u16) = (dbg!(parts[0]).trim().parse::<u16>().expect("Error during start conversion"),
                                 dbg!(parts[1]).trim().parse::<u16>().expect("Error during end conversion"));
        ranges.push(range);
        dbg!(range);
    }
}
