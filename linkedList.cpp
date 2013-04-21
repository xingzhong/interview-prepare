#include <stdio.h>
#include <stdlib.h>

typedef struct IntElement {
  struct IntElement *next;
  int data;
} IntElement;

int create (IntElement **head, int times) {
  IntElement *curr;
  int i;
  for (i=0; i<times; i++){
    curr = (IntElement *)malloc(sizeof(IntElement));
    curr->data = i;
    curr->next = *head;
    *head = curr;
  }
  return 1;
}

int walk (IntElement *head){
  printf("\nwalk\n");
  while(head){
    printf("%d\n", head->data);
    head = head->next;
  }
  return 1;
}

int insert (IntElement **head, int data){
  IntElement *curr, *swap;
  if ((*head)->next){
    curr = (IntElement *)malloc(sizeof(IntElement));
    curr->data = data;
    curr->next = (*head)->next;
    (*head)->next = curr;
  }
  return 1;
}

IntElement * reverse(IntElement *curr, IntElement *prev) {
  IntElement *swap;
  if (curr->next == NULL){
    curr->next = prev;
    return curr;
  } 
  else{
    swap = reverse(curr->next, curr);
    curr->next = prev;
    return swap;
  }
}

int main(){
  IntElement *list = NULL;
  create(&list, 10);
  walk(list);
  insert(&list, 99);
  walk(list);
  list = reverse(list, NULL);
  walk(list);

  return 1;
}
