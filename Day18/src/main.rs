use std::fs;
use std::cmp::max;
use std::convert::TryInto;

fn main() {
    let filename = "C:\\Users\\Steve\\Desktop\\Advent Of Code\\input\\Day18.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    
    // println!("{}", contents);
    let summands = contents.split('\n');
    let mut summand_vec = Vec::<Vec<[u32;2]>>::new();
    // let sum = read_snail_number(summands.next().unwrap_or_default().trim_end());
    // println!("{:?}", sum);
    
    for summand in summands {
        summand_vec.push(read_snail_number(summand.trim_end()));
    }

    let mut max_mag = 0;

    for i in 0..summand_vec.len()-1 {
        for j in i..summand_vec.len() {
            let mut s = calculate_magnitude(add_snail_number(&summand_vec[i], &summand_vec[j]));
            max_mag = max(s, max_mag);
            s = calculate_magnitude(add_snail_number(&summand_vec[j], &summand_vec[i]));
            max_mag = max(s, max_mag);
        }
    }
    println!("{}", max_mag)

}

fn read_snail_number(num_str: &str) -> Vec<[u32; 2]> {
    let mut num = Vec::<[u32;2]>::new();
    let mut depth = 0;
    for c in num_str.chars() {
        if c == '[' {
            depth += 1;
        } else if c == ']' {
            depth -= 1;
        } else if c != ',' {
            num.push([depth, c.to_digit(10).expect("Somehow char is not a number").try_into().unwrap()]);
        }
    }
    // println!("{:?}", num);
    num
}

fn add_snail_number(a: &Vec<[u32;2]>, b: &Vec<[u32;2]>) -> Vec<[u32; 2]> {
    let mut sum = Vec::<[u32;2]>::new();
    sum.extend(a);
    sum.extend(b);
    let mut reduced = false;
    for i in 0..sum.len() {
        sum[i][0] += 1
    }
    while !reduced {
        let mut exploded = false;
        for i in 0..sum.len()-1 {
            if sum[i][0] == 5 {
                if i > 0 {
                    sum[i-1][1] += sum[i][1];
                }
                sum[i] = [4, 0];
                let rightval = sum.remove(i+1)[1];
                if i < sum.len()-1 {
                    sum[i+1][1] += rightval;
                }
                exploded = true;
                // println!("{:?}", a);
                break;
            }
        }
        if exploded {
            continue;
        }
        let mut split = false;
        for i in 0..sum.len() {
            if sum[i][1] > 9 {
                let depth = sum[i][0] + 1;
                let leftval = sum[i][1] / 2;
                let rightval = (f64::from(sum[i][1]) / 2.0).ceil() as u32;
                sum[i] = [depth, leftval];
                sum.insert(i+1, [depth, rightval]);
                split = true;
                // println!("{:?}", a);
                break;
            }
        }
        if split {
            continue;
        }
        reduced = true;
    }
    sum
}

fn calculate_magnitude(mut num: Vec<[u32; 2]>) -> u32 {
    for i in (1..=4).rev() {
        let mut j = 0;
        while j <num.len() {
            if num[j][0] == i {
                num[j] = [i-1, num[j][1] * 3 + num.remove(j+1)[1] * 2];
            }
            j = j + 1;
        }
    }
    num[0][1]
}