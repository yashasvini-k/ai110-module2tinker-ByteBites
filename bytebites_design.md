# ByteBites UML Class Diagram

## Final Design
```mermaid
classDiagram
    class Customer {
        -name: string
        -purchaseHistory: Order[]
        +getName(): string
        +addPurchase(order: Order): void
        +getPurchaseHistory(): Order[]
    }
    class MenuItem {
        -name: string
        -price: float
        -category: string
        -popularityRating: float
        +getName(): string
        +getPrice(): float
        +getCategory(): string
        +getPopularityRating(): float
        +setPopularityRating(rating: float): void
    }
    class Menu {
        -items: MenuItem[]
        +addItem(item: MenuItem): void
        +removeItem(item: MenuItem): void
        +getAllItems(): MenuItem[]
        +filterByCategory(category: string): MenuItem[]
    }
    class Order {
        -selectedItems: MenuItem[]
        -totalCost: float
        +addItem(item: MenuItem): void
        +removeItem(item: MenuItem): void
        +computeTotalCost(): float
        +getTotalCost(): float
    }
    Customer "1" --> "*" Order : places
    Customer "*" --> "1" Menu : browses
    Order "*" --> "*" MenuItem : contains
    Menu "1" --> "*" MenuItem : manages
\\```
```



