fn main() {
    let mut numbers = vec![0,3,6];
    //println!("{}",numbers.len());
    while numbers.len() < 2020 {
        let last_number = *numbers.last().unwrap();
        let index_of_first_occurence = numbers.iter().position(|&x| x == last_number).unwrap();
        let index_of_last_number = numbers.len() - 1;
        if index_of_first_occurence == index_of_last_number {
            numbers.push(0);
        }
        else {
            let index_of_previous = numbers.len() - 2 - numbers[..(numbers.len()-1)].iter()
                                    .rev().position(|&x| x == last_number).unwrap();
            numbers.push(index_of_last_number - index_of_previous);
        }
    }
    //println!("{:?}", numbers);
    println!("{}", *numbers.last().unwrap());
}
