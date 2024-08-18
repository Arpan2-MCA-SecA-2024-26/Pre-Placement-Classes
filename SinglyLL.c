#include<stdio.h>
#include<malloc.h>
struct node{
	int data;
	struct node *next;
};
struct node *head=NULL;
void pushbeg()
{
	struct node *n=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter data to push:");
	scanf("%d",&n->data);
	if (head==NULL)
	{
		head=n;
		head->next=NULL;
	}
	else
	{
		n->next=head;
		head=n;
	}
}
void pushend()
{
	struct node *n=(struct node*)malloc(sizeof(struct node));
	printf("\nEnter data to push:");
	scanf("%d",&n->data);
	if (head==NULL)
	{
		head=n;
		head->next=NULL;
	}
	else
	{
		struct node *p=head;
		while(p->next!=NULL)
			p=p->next;
		p->next=n;
		n->next=NULL;
	}
}
void popbeg()
{
	if (head==NULL)
		printf("\nUnderflow");
	else
	{
		struct node *del=head;
		printf("\n%d has been deleted",del->data);
		head=head->next;
		free(del);
	}
}
void popend()
{
	if (head==NULL)
		printf("\nUnderflow");
	else if (head->next==NULL)
	{
		popbeg();
	}
	else
	{
		struct node *del=head;
		while(del->next->next!=NULL)
			del=del->next;
		printf("\n%d has been deleted",del->next->data);
		free(del->next);
		del->next=NULL;
	}
}
void pushpos()
{
	int	pos;
	printf("\nEnter position:");
	scanf("%d",&pos);
	if (pos==0)
		pushbeg();
	else
	{
		struct node *n=(struct node*)malloc(sizeof(struct node));
		printf("\nEnter data to push:");
		scanf("%d",&n->data);
		if (head==NULL)
		{
			head=n;
			head->next=NULL;
		}
		else
		{
			struct node *p=head;
			for (int i=1;i<pos;i++)
				p=p->next;
			n->next=p->next;
			p->next=n;
		}
	}	
}
void poppos(int pos)
{
	if (head==NULL)
		printf("\nUnderflow");
	else
	{
		if (pos==0)
			popbeg();
		else
		{
			struct node *p=head;
			for (int i=1;i<pos;i++)
				p=p->next;
			struct node *del=p->next;
			p->next=p->next->next;
			printf("\n%d has been deleted",del->data);
			free(del);
		}	
	}
}
void popdata()
{
	if (head==NULL)
		printf("\nUnderflow");
	else
	{
		int d,i=0,f=-1;
		printf("\nEnter data to delete:");
		scanf("%d",&d);
		struct node *p=head;
		while(p!=NULL)
		{
			if (p->data==d)
			{
				f=i;
				break;
			}
			else
			{
				p=p->next;
				i++;
			}
		}
		if (f==-1)
			printf("\nData not found");
		else
			poppos(f);	
	}
}
void disp()
{
	if (head==NULL)
		printf("\nEmpty");
	else
	{
		struct node *p=head;
		while(p!=NULL)
		{
			printf("%d-->",p->data);
			p=p->next;
		}
		printf("NULL\n");
	}
}

int main()
{
	printf("1. pushbeg\n2. pushend\n3. popbeg\n4. popend\n5. pushpos\n6. poppos\n7. popdata\n9. disp\n0. exit");
	while(1)
	{
		int ch;
		printf("\nEnter choice:");
		scanf("%d",&ch);
		if (ch==1)
			pushbeg();
		else if (ch==2)
			pushend();
		else if (ch==3)
			popbeg();
		else if (ch==4)
			popend();
		else if (ch==5)
			pushpos();
		else if (ch==6)
		{
			int pos;
			printf("\nEnter position:");
			scanf("%d",&pos);
			poppos(pos);
		}
		else if (ch==7)
			popdata();
		else if (ch==9)
			disp();
		else if (ch==0)
			break;
		else
			printf("\nInvalid choice");
	}
}
