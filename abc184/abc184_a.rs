use ::proconio::input;
fn main() {
    input! {
        a : i128,
        b : i128,
        c : i128,
        d : i128,
    }
    let ans: i128 = a * d - b * c;
    println!("{}", ans);
}
