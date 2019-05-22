import storage from 'redux-persist/es/storage';
import thunkMiddleware from 'redux-thunk';
import { applyMiddleware, compose, createStore } from 'redux';
import { persistReducer, persistStore } from 'redux-persist';
import { routerMiddleware } from 'connected-react-router';

import getRootReducer from 'reducers/reducers.jsx';
import authMiddleware from 'middleware/authMiddleware.jsx';

export default (history) => {
    const rootReducer = getRootReducer(history)

    const persistedReducer = persistReducer({
        key: 'polls',
        storage: storage,
        whitelist: [],
    }, rootReducer);

    // const persistedReducer = rootReducer;


    const store = createStore(
        persistedReducer,
        {},
        compose(
            applyMiddleware(
                authMiddleware,
                thunkMiddleware,
            ),
            window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
        )
    );

    const persistor = persistStore(store);

    return {store, persistor};
};