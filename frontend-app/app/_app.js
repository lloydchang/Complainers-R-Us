import * as React from "react";
import PropTypes from "prop-types";
import Head from "next/head";
import { AppProps } from "next/app";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";


const theme = createTheme({
  palette: {
    primary: {
      main: "#060f12",
    },
    secondary: {
      main: "#c6302c",
    },
    error: {
      main: "#f44336",
    },
    background: {
      default: "#f3e6cc",
    },
  },
});

export default function MyApp({ Component, pageProps }) {
    

    React.useEffect(() => {
        // Remove the server-side injected CSS.
        const jssStyles = document.querySelector("#jss-server-side");
        if (jssStyles) {
            jssStyles.parentElement.removeChild(jssStyles);
        }
    }
    , []);

    return (
        <React.Fragment>
            <Head>
                <title>Complainers R Us - Magical Retellers Peddling Rubies</title>
                <meta name="viewport" content="initial-scale=1, width=device-width" />
            </Head>
            <ThemeProvider theme={theme}>
                {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
                <CssBaseline />
                <Component {...pageProps} />
            </ThemeProvider>
        </React.Fragment>
    );
}

MyApp.propTypes = {
    Component: PropTypes.elementType.isRequired,
    pageProps: PropTypes.object.isRequired,
};