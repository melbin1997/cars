#include<stdio.h>
#include<malloc.h>

struct node{
	int coeff;
	int exp;
	struct node *next;
}*poly1,*poly2,*poly;

void create(){
	int c,p;
	char ch='y';
	struct node *new,*ptr;
	poly1->coeff=NULL;
	poly1->exp=NULL;
	ptr=poly1;
	printf("\nEnter the details of the first polynomial");
	while(ch=='y'||ch=='Y'){
		new=(struct node*)malloc(sizeof(struct node));
		printf("\nEnter the coefficient\t: ");
		scanf("%d",&new->coeff);
		printf("\nEnter the exponent\t: ");
		scanf("%d",&new->exp);
		ptr->next=new;
		ptr=ptr->next;
	}

}

void display(){
	struct node *ptr;
	ptr=poly1;
	while(poly1->next!=NULL){
		printf("Coefficient %d",ptr->coeff);
		printf("Exponent %d",ptr->exp);
		ptr=ptr->next;
	}
}

void main(){
	create();
	display();
}