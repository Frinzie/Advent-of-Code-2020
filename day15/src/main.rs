use std::collections::HashMap;

fn main() {
    let mut numbers = vec![0,14,1,3,7,9];
    numbers.reserve(30000000);
    
    // hashmap that holds (number:last_index) pairs
    let mut last_occurences: HashMap<usize, usize> = HashMap::new();
    for i in 0..numbers.len()-1 {
        last_occurences.insert(numbers[i] as usize, i);
    }

    // probably faster than having to call .len() every time
    let mut index_of_last_number = numbers.len() - 1;
    while numbers.len() < 30000000 {
        let last_number = *numbers.last().unwrap();
        // checks if last number hasn't been added before
        if !last_occurences.contains_key(&last_number) {
            numbers.push(0);
        }
        else {
            let index_of_previous = *last_occurences.get(&last_number).unwrap();
            numbers.push(index_of_last_number - index_of_previous);
        }
        // important to note: this is the last number, not the new one!
        // since adding the new one would screw up the check in next
        // iteration
        last_occurences.insert(last_number, index_of_last_number);
        index_of_last_number += 1; // add 1 since there's a new element
    }
    // println!("{:?}", numbers);
    println!("{}", *numbers.last().unwrap());
}
