import Control.Monad.State


data Tree a = Leaf a | Fork (Tree a) a (Tree a) deriving (Show)

test_tree1 = (Fork (Leaf ()) () (Leaf ()))
test_tree2 = Leaf ()


numberTree :: Tree () -> Tree Integer
numberTree tree = (evalState $ (countState tree)) 1

countState :: Tree () -> State (Integer) (Tree Integer)
countState (Leaf _) = do
    number <- get
    modify succ
    return $ Leaf number
    
countState (Fork left _ right) = do
    left' <- countState left
    number <- get 
    modify succ
    right' <- countState right
    return $ Fork left' number right'

