use std::io;

fn main() {
    let mut input: String = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Unable to read from 'stdin'!");

    let size: u32 = input
        .trim()
        .parse()
        .expect("Error during conversion to u32");

    let mut ranges: Vec<(usize, usize)> = Vec::new();
    for _ in 0..size {
        let mut input: String = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Unable to read range from stdin");

        let range = parse_to_pair(input);
        ranges.push(range);
    }
    println!("{}", get_max_pixels(&ranges));
}

/// Function to get maximum square of non-blurred pixels
fn get_max_pixels(ranges: &Vec<(usize, usize)>) -> u32 {
    let mut result: u32 = 0;

    let mut previous: Vec<u32> = vec![0; ranges.len()];
    let (prev_start, prev_end): (usize, usize) = ranges[0];
    for idx in prev_start..(prev_end + 1) {
        previous[idx] = 1;
    }

    for i in 1..ranges.len() {
        let mut current: Vec<u32> = vec![0; ranges.len()];
        let (range_start, range_end): (usize, usize) = ranges[i];
        current[range_start] = 1;

        for j in (range_start + 1)..(range_end + 1) {
            let up: u32 = previous[j];
            let left: u32 = *current.get(j - 1).unwrap_or(&(0 as u32));
            let diag: u32 = *previous.get(j - 1).unwrap_or(&(0 as u32));

            match vec![left, up, diag].iter().min() {
                Some(min_value) => {
                    current[j] = *min_value + 1;
                    result = std::cmp::max(result, current[j])
                }
                None => {}
            }
        }
        previous = current;
    }
    result
}

/// Parse strings like "1 3\n" to tuple (1, 3)
/// Panic if any conversion failed.
fn parse_to_pair(string: String) -> (usize, usize) {
    let parts: Vec<&str> = string.split(' ').collect();
    let range: (usize, usize) = (
        parts[0]
            .trim()
            .parse::<usize>()
            .expect("Error during first conversion"),
        parts[1]
            .trim()
            .parse::<usize>()
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
