// https://github.com/TheAlgorithms/Rust/blob/master/src/sorting/quick_sort.rs

// MIT License

// Copyright (c) 2019 The Algorithms

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


pub fn partition<T: PartialOrd>(arr: &mut [T], lo: isize, hi: isize) -> isize {
    let pivot = hi as usize;
    let mut i = lo - 1;
    let mut j = hi;

    loop {
        i += 1;
        while arr[i as usize] < arr[pivot] {
            i += 1;
        }
        j -= 1;
        while j >= 0 && arr[j as usize] > arr[pivot] {
            j -= 1;
        }
        if i >= j {
            break;
        } else {
            arr.swap(i as usize, j as usize);
        }
    }
    arr.swap(i as usize, pivot as usize);
    i
}
fn _quick_sort<T: Ord>(arr: &mut [T], lo: isize, hi: isize) {
    if lo < hi {
        let p = partition(arr, lo, hi);
        _quick_sort(arr, lo, p - 1);
        _quick_sort(arr, p + 1, hi);
    }
}
pub fn quick_sort<T: Ord>(arr: &mut [T]) {
    let len = arr.len();
    _quick_sort(arr, 0, (len - 1) as isize);
}