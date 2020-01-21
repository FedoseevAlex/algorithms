use std::dbg;
use std::io;

fn main() {
    let mut input: String = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Unable to read from 'stdin'!");

    let size: u16 = input
        .trim()
        .parse()
        .expect("Error during conversion to u16");
    dbg!(size);

    let mut ranges: Vec<(u16, u16)> = Vec::new();
    for _ in 0..size {
        let mut input: String = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Unable to read range from stdin");

        let range = parse_to_pair(input);
        ranges.push(range);
        dbg!(range);
    }
}

/// Parse strings like "1 3\n" to tuple (1, 3)
/// Panic if any conversion failed.
fn parse_to_pair(string: String) -> (u16, u16) {
    let parts: Vec<&str> = string.split(' ').collect();
    let range: (u16, u16) = (
        dbg!(parts[0])
            .trim()
            .parse::<u16>()
            .expect("Error during first conversion"),
        dbg!(parts[1])
            .trim()
            .parse::<u16>()
            .expect("Error during second conversion"),
    );
    range
}

#[cfg(test)]
mod test_parse_to_pair {
    use super::*;

    #[test]
    fn correct_input() {
        assert_eq!(parse_to_pair("1 3".to_string()), (1, 3));
        assert_eq!(parse_to_pair("1 2 3".to_string()), (1, 2));
    }

    #[test]
    #[should_panic(expected = "Error during first conversion")]
    fn too_big_input() {
        assert_eq!(parse_to_pair("99999999 9999999999".to_string()), (1, 3));
    }

    #[test]
    #[should_panic(expected = "Error during first conversion")]
    fn negative_parse_1() {
        parse_to_pair("asdf".to_string());
    }

    #[test]
    #[should_panic(expected = "Error during second conversion")]
    fn negative_parse_2() {
        parse_to_pair("1 asdf".to_string());
    }
}
