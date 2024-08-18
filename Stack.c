#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define SIZE 10

int push(int);
void pop();
void display();
int stack[SIZE],top=-1,ch,val;

void main()
{
	
	while(1){
	
		printf("STACK OPERATIONS :-\n");
		printf("1.Push \n2.Pop \n3.Display \n4.Exit\n");
		printf("Enter the choice :");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:printf("Enter the data");
			scanf("%d",&val);
			push(val);
			break;
			case 2:pop();
			break;
			case 3:display();
			break;
			case 4:printf("Exited");exit(0);
			break;
			default:printf("Wrong Choice !!");
		}
	}
}
int push(int x)
{
	if(top==SIZE-1)
	{
		printf("Overflow");
	}
	else
	{
		stack[++top]=val;
		printf("Insertion Success");
	}
	
}
void pop()
{
	if(top==-1)
	{
		printf("Underflow");
	}
	else
	{
		printf("deleted data %d",stack[top--]);
	}
}
void display()
{
	if(top==-1)
	{
		printf("Underflow");
	}
	else
	{
		printf("Stack Elements are::-");
		for(int i=top;i>=0;i--)
		{
			printf("%d\n",stack[i]);
		}
	}
 }
