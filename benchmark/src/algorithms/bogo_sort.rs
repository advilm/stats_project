use rand::{prelude::SliceRandom, thread_rng};

pub fn bogo_sort<T: Ord>(arr: &mut [T]) {
    let mut rng = thread_rng();
    while !crate::is_sorted(arr) {
        arr.shuffle(&mut rng);
    }
}
