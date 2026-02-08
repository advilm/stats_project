// https://github.com/TheAlgorithms/Rust/blob/master/src/sorting/heap_sort.rs

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

pub fn heap_sort<T: Ord>(arr: &mut [T]) {
    if arr.len() <= 1 {
        return; // already sorted
    }

    heapify(arr);

    for end in (1..arr.len()).rev() {
        arr.swap(0, end);
        move_down(&mut arr[..end], 0);
    }
}

/// Convert `arr` into a max heap.
fn heapify<T: Ord>(arr: &mut [T]) {
    let last_parent = (arr.len() - 2) / 2;
    for i in (0..=last_parent).rev() {
        move_down(arr, i);
    }
}

/// Move the element at `root` down until `arr` is a max heap again.
///
/// This assumes that the subtrees under `root` are valid max heaps already.
fn move_down<T: Ord>(arr: &mut [T], mut root: usize) {
    let last = arr.len() - 1;
    loop {
        let left = 2 * root + 1;
        if left > last {
            break;
        }
        let right = left + 1;
        let max = if right <= last && arr[right] > arr[left] {
            right
        } else {
            left
        };

        if arr[max] > arr[root] {
            arr.swap(root, max);
        }
        root = max;
    }
}