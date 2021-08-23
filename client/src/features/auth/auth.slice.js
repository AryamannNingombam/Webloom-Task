import {
    createAsyncThunk,
    createSlice
} from '@reduxjs/toolkit';
import {
    CheckVerified,
    SignIn
} from '../../services/auth.service';

const initialState = {
    token: null,
    signedIn: false,
    verified:false,
};


export const SignInUser = createAsyncThunk(
    'auth/SignInUser',
    async (body) => {
        const response = await SignIn(body);
        const check = await CheckVerified(body.username);
        return {
            tokenData : response.data,
            check : check.data  
        };
    }
);

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        changeToken: (state, action) => {
            state.token = action.payload.token;
        },

    },
    extraReducers: (builder) => {
        builder
            .addCase(SignInUser.fulfilled, (state, action) => {
                state.token = action.payload.tokenDatatoken;
                state.verified = action.payload.check.verified;

            })
            .addCase(SignInUser.rejected, (state, action) => {
                console.log("REJECTED");
                state.token = null;
                state.signedIn = false;
            })


    },
});

export const {
    changeToken
} = authSlice.actions;


export default authSlice.reducer;