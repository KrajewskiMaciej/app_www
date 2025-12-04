import graphene
from graphene_django import DjangoObjectType
from posts.models import Post, Topic
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = ("id", "name", "description")
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))

    posts_by_title_contains = graphene.List(PostType, substr=graphene.String(required=True))
    posts_count_by_user = graphene.Int(user_id=graphene.Int(required=True))
    posts_by_user = graphene.List(PostType, user_id=graphene.Int(required=True))

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_post_by_id(root, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return None

    def resolve_posts_by_title_contains(root, info, substr):
        return Post.objects.filter(title__icontains=substr)

    def resolve_posts_count_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id).count()

    def resolve_posts_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id)

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        topic_id = graphene.Int(required=True)
        author_id = graphene.Int(required=True)

    post = graphene.Field(PostType)
    def mutate(self, info, title, topic_id, text, author_id):
        user = User.objects.get(pk=author_id)
        topic = Topic.objects.get(pk=topic_id)
        post = Post.objects.create(title=title, topic=topic,  text=text, created_by=user)
        return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title=None, content=None):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

        if title:
            post.title = title
        if content:
            post.content = content

        post.save()
        return UpdatePost(post=post)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            post = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

        post.delete()
        return DeletePost(ok=True)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)