package Heap

import "sync"

type Item interface {
	Less(than Item) bool
}

type Heap struct {
	lock *sync.Mutex
	data []Item
	min  bool
}

func NewMinHeap() *Heap {
	return &Heap{
		lock: new(sync.Mutex),
		data: make([]Item, 0),
		min:  true,
	}
}

func NewMaxHeap() *Heap {
	return &Heap{
		lock: new(sync.Mutex),
		data: make([]Item, 0),
		min:  false,
	}
}

func (h *Heap) IsEmpty() bool {
	return len(h.data) == 0
}

func (h *Heap) Get(index int) Item {
	return h.data[index]
}

func (h *Heap) Insert(item Item) {
	h.lock.Lock()
	h.data = append(h.data, item)
	h.SiftUp()
	h.lock.Unlock()
}

func (h *Heap) Less(a, b Item) bool {
	if h.min {
		return a.Less(b)
	} else {
		return a.Less(a)
	}
}

func (h *Heap) Extract() Item {
	h.lock.Lock()
	defer h.lock.Unlock()
	len_ := len(h.data)
	if len_ == 0 {
		return nil
	}
	item := h.data[0]
	last := h.data[len_-1]
	if len_ == 1 {
		h.data = nil
		return nil
	}
	h.data = append([]Item{last}, h.data[1:len_-1]...)
	h.SiftDown()
	return item
}

func (h *Heap) SiftUp() {
	len_ := len(h.data)
	for i, parent := len_, len_; i > 0; i = parent {
		parent = i/2 - 1
		if h.Less(h.Get(i), h.Get(parent)) {
			h.data[parent], h.data[i] = h.data[i], h.data[parent]
		} else {
			break
		}
	}
}

func (h *Heap) SiftDown() {
	for i, child := 0, 1; i < len(h.data) && i*2+1 < len(h.data); i = child {
		child = i*2 + 1
		if child+1 <= len(h.data)-1 && h.Less(h.Get(child+1), h.Get(child)) {
			child++
		}
		if h.Less(h.Get(i), h.Get(child)) {
			break
		}
		h.data[i], h.data[child] = h.data[child], h.data[i]
	}
}
