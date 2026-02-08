use benchmark::algorithms::*;

fn main() {
    let mut arr: Vec<_> = (0..1000).collect();
    bogo_sort(&mut arr);
    // dbg!(arr);
}
