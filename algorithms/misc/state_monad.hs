import Control.Monad.State (State, state)

data Direction = North | East | West | South deriving (Eq, Show)

dirs = [North, South, South, East, West, North] 

--push :: Direction -> State [Direction] ()
--push d = state $ helper d 
--    where

helper :: Direction -> [Direction] -> State [Direction] ()
helper North (South: ds) = state $ \_ -> ((), ds)
helper South (North: ds) = state $ \_ -> ((), ds)
helper East (West: ds) = state $ \_ -> ((), ds)
helper West (East: ds) = state $ \_ -> ((), ds)
helper d ds = state $ \_ -> ((), (d: ds))
        
-- dd :: [Direction] -> State [Direction] ()
-- dd [] = return []
-- dd (d: ds) = do
--     push d
--     dd ds


    
