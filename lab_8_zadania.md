### Pobranie wszystkich postów:
```
query {
  allPosts {
    id
    title
    text
    createdBy {
      id
      username
    }
  }
}
```

### Pobranie posta o id = 5:
```
query {
  postById(id: 5) {
    id
    title
  }
}
```

### Pobranie postów z daną frazą:
```
query {
  postsByTitleContains(substr: "test") {
    id
    title
  }
}
```

### Pobranie ilości postów danego autora:
```
query {
  postsCountByUser(userId: 1)
}
```

### Pobranie postów danego autora:
```
query {
  postsByUser(userId: 1) {
    id
    title
  }
}
```

### Dodanie nowego posta:
```
mutation {
  createPost(title: "Nowy post", topicId: 2 ,text: "Treść", authorId: 1) {
    post {
      id
      title
      topic {
        id 
        name
      }
    }
  }
}
```

### Edycja posta:
```
mutation {
  updatePost(id: 6, title: "Zmieniony tytuł") {
    post {
      id
      title
    }
  }
}
```

### Usunięcie posta:
```
mutation {
  deletePost(id: 5) {
    ok
  }
}
```