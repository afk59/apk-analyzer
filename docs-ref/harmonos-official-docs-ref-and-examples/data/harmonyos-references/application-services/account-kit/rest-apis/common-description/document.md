# Common Description

#### TLS Protocol and Cipher Suites

| 
TLS Version

 | 

Cipher Suite (IANA Name)

 |
| :-- | :-- |
| 

TLS1.2

 | 

TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256

 |

#### Environment Configuration for the Sample Code

Configure the environment as follows before running the sample code provided by REST APIs:

-   Configure Maven dependencies.
    
    <dependencies>
        <dependency>
            <groupId>com.alibaba.fastjson2</groupId>
            <artifactId>fastjson2</artifactId>
            <version>2.0.51</version> <!--Use the version required by your project.-->
        </dependency>
        <dependency>
            <groupId>org.apache.httpcomponents</groupId>
            <artifactId>httpclient</artifactId>
            <version>4.5.6</version> <!--Use the version required by your project.-->
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.26</version> <!--Use the version required by your project.-->
        </dependency>
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.2.11</version> <!--Use the version required by your project.-->
        </dependency>
    </dependencies>
    
-   Import the **CallUtils** utility class. (Place this utility class and the API sample code in the same directory. If not, manually add the **import** statement to the API sample code.)
    
    import com.alibaba.fastjson2.JSON;
    import com.alibaba.fastjson2.JSONObject;
    import lombok.extern.slf4j.Slf4j;
    import org.apache.http.Header;
    import org.apache.http.HttpEntity;
    import org.apache.http.HttpStatus;
    import org.apache.http.client.config.RequestConfig;
    import org.apache.http.client.methods.CloseableHttpResponse;
    import org.apache.http.client.methods.HttpUriRequest;
    import org.apache.http.config.Registry;
    import org.apache.http.config.RegistryBuilder;
    import org.apache.http.conn.socket.ConnectionSocketFactory;
    import org.apache.http.conn.socket.PlainConnectionSocketFactory;
    import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
    import org.apache.http.entity.ContentType;
    import org.apache.http.entity.StringEntity;
    import org.apache.http.impl.client.CloseableHttpClient;
    import org.apache.http.impl.client.HttpClients;
    import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
    import org.apache.http.util.EntityUtils;
    import javax.net.ssl.SSLContext;
    import javax.net.ssl.TrustManagerFactory;
    import java.io.IOException;
    import java.security.KeyManagementException;
    import java.security.KeyStore;
    import java.security.KeyStoreException;
    import java.security.NoSuchAlgorithmException;
    import java.util.Map;
    import java.util.Objects;
    import java.util.function.BiFunction;
    
    /\*\*
     \* HTTP utility class.
     \*/
    @Slf4j
    public class CallUtils {
        public static String remoteCall(HttpUriRequest request) throws IOException {
            return remoteCall(request, CallUtils::nspErrorHandler);
        }
    
        public static String remoteCallOAuth(HttpUriRequest request) throws IOException {
            return remoteCall(request, CallUtils::oauthErrorHandler);
        }
    
        public static String remoteCallAccountApi(HttpUriRequest request) throws IOException {
            return remoteCall(request, CallUtils::accountApiErrorHandler);
        }
    
        public static <E extends Exception> String remoteCall(HttpUriRequest request,
            BiFunction<CloseableHttpResponse, String, E> errorHandler) throws IOException, E {
            try (CloseableHttpResponse response = getClient().execute(request)) {
                HttpEntity responseEntity = response.getEntity();
                String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
                EntityUtils.consume(responseEntity);
                if (errorHandler != null) {
                    E error = errorHandler.apply(response, ret);
                    if (null != error) {
                        throw error;
                    }
                }
                return ret;
            }
        }
    
        public static JSONObject toJsonObject(String json) {
            return (JSONObject) JSON.parse(json);
        }
    
        public static StringEntity wrapJsonEntity(Object obj) {
            return new StringEntity(CallUtils.toJsonString(obj), ContentType.create("application/json", "UTF-8"));
        }
    
        public static String toJsonString(Object obj) {
            return JSON.toJSONString(obj);
        }
    
        public static IOException nspErrorHandler(CloseableHttpResponse response, String rawBody) {
            int statusCode = response.getStatusLine().getStatusCode();
            if (statusCode != 200) {
                return new IOException("call failed! status:" + statusCode + ", response data: " + rawBody);
            }
            Header nspStatus = response.getFirstHeader("NSP\_STATUS");
            if (Objects.nonNull(nspStatus)) {
                return new IOException("call failed! nsp\_status:" + nspStatus.getValue() + ", response data: " + rawBody);
            }
            return null;
        }
    
        public static IOException oauthErrorHandler(CloseableHttpResponse response, String rawBody) {
            int statusCode = response.getStatusLine().getStatusCode();
            // If the returned HTTP status code is **200**, the request is successful.
            if (statusCode == HttpStatus.SC\_OK) {
                return null;
            }
            // If the returned HTTP status code is not **200**, parse the response body and execute error handling logic according to service needs.
            Map<String, Object> errorResponseBody = CallUtils.toJsonObject(rawBody);
            // Error code.
            Object error = errorResponseBody.get("error");
            // Sub-error code.
            Object subError = errorResponseBody.get("sub\_error");
            // You can customize error handling based on the returned error and sub-error codes, for example, throwing an exception.
            if (Objects.nonNull(error) && Objects.nonNull(subError)) {
                return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
            }
            return null;
        }
    
        public static IOException accountApiErrorHandler(CloseableHttpResponse response, String rawBody) {
            int statusCode = response.getStatusLine().getStatusCode();
            // If the returned HTTP status code is not **200**, the request fails.
            if (statusCode != 200) {
                return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
            }
           // If the returned HTTP status code is **200**, parse the response body and determine the service error code.
            JSONObject errorResponseBody = CallUtils.toJsonObject(rawBody);
            // Result code.
            Integer resultCode = errorResponseBody.getInteger("resultCode");
            // The value **0** of **resultCode** indicates a success, and a value other than 0 indicates a failure.
            if (Objects.nonNull(resultCode) && resultCode != 0) {
                return new IOException("call failed! http status code: " + statusCode + ", response data: " + rawBody);
            }
            return null;
        }
    
        private static CloseableHttpClient getClient() {
            PoolingHttpClientConnectionManager connectionManager = buildConnectionManager(
                new String\[\] {"TLSv1.2"}, new String\[\] {
                    "TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384", "TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256",
                    "TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384", "TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256"
                });
            connectionManager.setMaxTotal(400);
            connectionManager.setDefaultMaxPerRoute(400);
            RequestConfig config = RequestConfig.custom()
                .setConnectionRequestTimeout(100)
                .setRedirectsEnabled(false)
                .build();
            return HttpClients.custom()
                .useSystemProperties()
                .setConnectionManager(connectionManager)
                .setDefaultRequestConfig(config)
                .build();
        }
    
        private static PoolingHttpClientConnectionManager buildConnectionManager(String\[\] supportedProtocols,
            String\[\] supportedCipherSuites) {
            PoolingHttpClientConnectionManager connectionManager = null;
            try {
                SSLContext sc = SSLContext.getInstance("TLSv1.2");
                TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
                tmf.init((KeyStore) null);
                sc.init(null, tmf.getTrustManagers(), null);
                SSLConnectionSocketFactory sslsf = new SSLConnectionSocketFactory(sc, supportedProtocols,
                    supportedCipherSuites, SSLConnectionSocketFactory.getDefaultHostnameVerifier());
                Registry<ConnectionSocketFactory> registry = RegistryBuilder.<ConnectionSocketFactory>create()
                    .register("http", new PlainConnectionSocketFactory())
                    .register("https", sslsf)
                    .build();
                connectionManager = new PoolingHttpClientConnectionManager(registry);
            } catch (NoSuchAlgorithmException | KeyStoreException | KeyManagementException e) {
                log.error("build connect manager failed", e);
            }
            return connectionManager;
        }
    }
