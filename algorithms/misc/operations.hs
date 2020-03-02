import Control.Monad.State
data Direction = North | East | West | South deriving (Eq, Show)

dirs = [North, South, South, East, West, North]

-- dirReduce :: [Direction] -> [Direction]
-- dirReduce ds = (snd . runState) (mapM push ds)

push :: Direction -> State [Direction] ()
push d' = do 
  (d: ds) <- get
  case d' of
    North | d == South -> put ds
    South | d == North -> put ds 
    East  | d == West  -> put ds
    West  | d == East  -> put ds
    _                  -> put (d': d: ds)
  
    
