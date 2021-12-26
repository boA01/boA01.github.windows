package ArrayList

import (
	"fmt"
	"errors"
)

type ArrayList struct{
	dataStore []interface{}
	theSize int
}

func NewArray() *ArrayList{
	list := new(ArrayList)
	list.dataStore = make([]interface{}, 0, 10)
	list.theSize = 0
	return list
}

func (list *ArrayList) Size() int{
	return list.theSize
}

func (list *ArrayList) Append(newVal interface{}){
	list.dataStore=append(list.dataStore, newVal)
	list.theSize++
}

func (list *ArrayList) Get(index int) (interface{}, error){
	if index<0 || index>list.theSize{
		return nil, errors.New("索引异常")
	} else{
		return list.dataStore[index], nil
	}
}

func (list *ArrayList) String() string{
	return fmt.Sprint(list.dataStore)
}

func (list *ArrayList) Set(index int, newVal interface{}) error{
	if index<0 || index>list.theSize{
		return errors.New("索引异常")
	} else{
		list.dataStore[index] = newVal
	}
	return nil
}

func (list *ArrayList) Insert(index int, newVal interface{}) error{
	if index<0 || index>list.theSize{
		return errors.New("索引异常")
	} else if index==cap(list.dataStore) {
		newdataStore := make([]interface{}, index, 2*index)
		copy(newdataStore, list.dataStore)
		list.dataStore = newdataStore
		list.dataStore[index] = newVal
		list.theSize++
		return nil
	} else if index==0{
		newarr := []interface{}{index}
		list.dataStore = append(newarr, list.dataStore[:]...)
		list.theSize++
		return nil
	}
	var rarr []interface{}
	rarr = append(rarr, list.dataStore[index:]...)

	list.dataStore[index] = newVal
	larr := list.dataStore[:index+1]

	list.dataStore = append(larr, rarr...)
	list.theSize++
	return nil
}

func (list *ArrayList) Delete(index int) error{
	if index<0 || index>list.theSize{
		return errors.New("索引异常")
	}
	list.dataStore = append(list.dataStore[:index], list.dataStore[index+1:]...)
	list.theSize--
	return nil
}

func (list *ArrayList) Clear(){
	list = NewArray()
}
