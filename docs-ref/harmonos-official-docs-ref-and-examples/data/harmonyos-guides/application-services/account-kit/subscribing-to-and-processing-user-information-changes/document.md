# Subscribing to and Processing User Information Changes

#### Overview

By subscribing to user information changes, your app can receive important updates about users and their accounts. When there are changes to a user or their account information, the Account Kit server sends a notification to the app server, and the app server can respond accordingly.

#### User Information Change Events

| 
Notification Event

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

tokens-revoked

 | 

https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked

 | 

A user revokes authorization on an app.

 |
| 

account-purged

 | 

https://schemas.openid.net/secevent/risc/event-type/account-purged

 | 

A user deregisters a HUAWEI ID.

 |
| 

phone-modified

 | 

https://schemas.openid.net/secevent/oauth/event-type/phone-modified

 | 

A user changes their authorized mobile number.

 |

#### Subscribing to User Information Changes

The subscription procedure is as follows:

1.  Sign in to [HUAWEI Developers](https://developer.huawei.com/consumer/en/), access its console from the upper right corner, and choose **API services** > **API Library**.
2.  Find RISC under **App Services**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/yQHokAUuSyWbjnAaatWJwA/en-us_image_0000002528823299.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D352BDD537A4C6FD879D2CA9A8527F61C056B3FC27F12688663BC9518B04245 "Click to enlarge")
    
3.  Click **Enable**. (You need to select a project first.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/Roj3FzT_TUWe_VDUts9Oww/en-us_image_0000002528943269.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23189D238E0554CE509895D897EE25D71D8A606EBD8FC45004F4B6503B1689EB "Click to enlarge")
    
4.  Click **Subscribe to notification**. In the window that is displayed, set the callback URL and subscription scope.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/0g7SxLmMTFCEzS9rWj53BA/en-us_image_0000002528943271.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A079181A9B14D38F03346D83B186EAEDBF9A5C774F4F7809013AA696A052382 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/iCAxQXmeRNaXtKmipB0GSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A7C4AE65233CE9CD33602A1028176707D78A358A0BF6C6ECD1827CD3DA1CA80)
    
    Callback URL: address that receives notifications upon user information changes.
    
    Subscription scope: user information change events. For details, please refer to [User Information Change Events](#section824594942618).
    

#### Processing Notifications

The Account Kit server sends a message to your app server. After receiving the message, your app server performs signature verification on the token in the message header to ensure that the message is complete and valid. Then, your app server parses the message to obtain the user information change event details. The procedure is as follows:

1.  **Perform signature verification on the token in the message header.**
    
    Use any JWT library (for example, [jwt.io](https://jwt.io/introduction/)) to decode and verify the signature.
    
    No matter which library is used, you must perform the following operations:
    
    1.  Call the **https:// risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration** API to obtain the issuer ID (**issuer**) and signature key certificate URI (**jwks\_uri**).
    2.  Use the JWT library, which you have added as a dependency, to parse the access token in the message header and obtain the key ID of the signature.
    3.  Use the key ID to obtain the public key of the JWT signature from the signature key certificate URI.
    4.  Check whether the value of **aud** in the JWT signature is the same as the client ID provided in [Subscribing to User Information Changes](#section1430414972716).
    5.  Verify that the issuer in the JWT signature is the same as the value of **issuer** previously obtained.
    
    Check the following sample code to learn more about the signature verification logic:
    
    Maven Dependency Configurations
    
    <dependencies>
       <dependency>
          <groupId>com.github.ben-manes.caffeine</groupId>
          <artifactId>caffeine</artifactId>
          <version>2.9.3</version> <!--Use the version required by your project.-->
       </dependency>
       <dependency>   
          <groupId>com.auth0</groupId> 
          <artifactId>jwks-rsa</artifactId>
          <version>0.21.2</version> <!--Use the version required by your project.-->
       </dependency>
       <dependency>
          <groupId>io.jsonwebtoken</groupId>
          <artifactId>jjwt-impl</artifactId>
          <version>0.11.5</version> <!--Use the version required by your project.-->
       </dependency>
       <dependency>
          <groupId>io.jsonwebtoken</groupId>
          <artifactId>jjwt-jackson</artifactId>
          <version>0.11.5</version> <!--Use the version required by your project.-->
       </dependency>
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
    
    Java Sample Code for Signature Verification
    
    import com.alibaba.fastjson2.JSON;
    import com.alibaba.fastjson2.JSONObject;
    import com.auth0.jwk.JwkProvider;
    import com.auth0.jwk.UrlJwkProvider;
    import com.github.benmanes.caffeine.cache.CacheLoader;
    import com.github.benmanes.caffeine.cache.Caffeine;
    import com.github.benmanes.caffeine.cache.LoadingCache;
    import io.jsonwebtoken.Claims;
    import io.jsonwebtoken.IncorrectClaimException;
    import io.jsonwebtoken.JwsHeader;
    import io.jsonwebtoken.Jwt;
    import io.jsonwebtoken.JwtParser;
    import io.jsonwebtoken.Jwts;
    import io.jsonwebtoken.SigningKeyResolver;
    import io.jsonwebtoken.security.SignatureException;
    import lombok.Data;
    import lombok.extern.slf4j.Slf4j;
    import org.apache.http.HttpEntity;
    import org.apache.http.HttpStatus;
    import org.apache.http.client.config.RequestConfig;
    import org.apache.http.client.methods.CloseableHttpResponse;
    import org.apache.http.client.methods.HttpGet;
    import org.apache.http.config.Registry;
    import org.apache.http.config.RegistryBuilder;
    import org.apache.http.conn.socket.ConnectionSocketFactory;
    import org.apache.http.conn.socket.PlainConnectionSocketFactory;
    import org.apache.http.conn.ssl.SSLConnectionSocketFactory;
    import org.apache.http.impl.client.CloseableHttpClient;
    import org.apache.http.impl.client.HttpClients;
    import org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
    import org.apache.http.util.EntityUtils;
    import org.checkerframework.checker.nullness.qual.NonNull;
    import org.checkerframework.checker.nullness.qual.Nullable;
    import javax.net.ssl.SSLContext;
    import javax.net.ssl.TrustManagerFactory;
    import java.io.IOException;
    import java.net.URL;
    import java.security.Key;
    import java.security.KeyManagementException;
    import java.security.KeyStore;
    import java.security.KeyStoreException;
    import java.security.NoSuchAlgorithmException;
    import java.security.PublicKey;
    import java.util.Objects;
    import java.util.concurrent.TimeUnit;
    
    /\*\*
     \* Subscribe to and process user information changes.
     \*/
    @Slf4j
    public class RiscDemo {
        /\*\*
         \* Public configuration URL.
         \*/
        private static final String PUBLIC\_CONFIGURATION\_URL = "https://risc.cloud.huawei.com/v1beta/public/risc/.well-known/risc-configuration";
    
        /\*\*
         \* Public configuration cache.
         \*/
        private final LoadingCache<String, PublicConfiguration> publicConfigurationCache = Caffeine.newBuilder()
                .expireAfterWrite(1, TimeUnit.DAYS)
                .build(key -> {
                    HttpGet request = new HttpGet(PUBLIC\_CONFIGURATION\_URL);
                    try (CloseableHttpResponse response = getClient().execute(request)) {
                        HttpEntity responseEntity = response.getEntity();
                        String ret = responseEntity != null ? EntityUtils.toString(responseEntity) : null;
                        EntityUtils.consume(responseEntity);
                        int statusCode = response.getStatusLine().getStatusCode();
                        // If the HTTP status code is not 200, an exception is thrown.
                        if (statusCode != HttpStatus.SC\_OK) {
                            throw new IOException("call failed! http status code: " + statusCode + ", response data: " + ret);
                        }
                        JSONObject configJson = (JSONObject) JSON.parse(ret);
                        if (configJson == null) {
                            throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
                        }
                        String issuer = configJson.getString("issuer");
                        String jwksUri = configJson.getString("jwks\_uri");
                        if (Objects.isNull(issuer) || Objects.isNull(jwksUri)) {
                            throw new IllegalArgumentException("response param error! http status code: " + statusCode + ", response data: " + ret);
                        }
                        PublicConfiguration publicConfiguration = new PublicConfiguration();
                        publicConfiguration.setIssuer(issuer);
                        publicConfiguration.setJwksUri(jwksUri);
                        return publicConfiguration;
                    }
                });
    
        /\*\*
         \* Public key cache.
         \*/
        private final LoadingCache<String, PublicKey> publicKeyCache = Caffeine.newBuilder()
                .expireAfterWrite(1, TimeUnit.DAYS)
                .build(new CacheLoader<String, PublicKey>() {
                    @Override
                    public @Nullable PublicKey load(@NonNull String key) throws Exception {
                        PublicConfiguration publicConfiguration = getPublicConfiguration();
                        JwkProvider huaweiCerts = new UrlJwkProvider(new URL(publicConfiguration.getJwksUri()), null, null);
                        return huaweiCerts.get(key).getPublicKey();
                    }
                });
    
        /\*\*
         \* Entry point of the debugging method.
         \* @param args Input parameters of the main method.
         \*/
        public static void main(String\[\] args) {
            // <token> in Authorization: Bearer <token> of the request header.
            String token = "_<token>_";
            // Client ID
            String clientId = "_<Client ID>_";
            Jwt<?, ?> jwt = new RiscDemo().validateSecurityEventToken(token, clientId);
            if (Objects.isNull(jwt)) {
                // Signature verification failed.
                log.error("verify sign failed");
            } else {
                // Signature verification succeeded.
                log.info("verify sign success");
            }
        }
    
        /\*\*
         \* Perform signature verification on the token in the Authorization header field.
         \*
         \* @param token    <token> from Authorization: Bearer <token> in the message header.
         \* @param clientId clientId
         \* @return If null is returned, the verification fails. Otherwise, the verification is successful.
         \*/
        public Jwt<?, ?> validateSecurityEventToken(String token, String clientId) {
            try {
                // Value of issuer in the public configuration.
                String issuer = getPublicConfiguration().getIssuer();
                SigningKeyResolver signingKeyResolver = new SigningKeyResolver() {
                    private PublicKey getPublicKey(JwsHeader<?> jwsHeader) {
                        try {
                            return publicKeyCache.get(jwsHeader.getKeyId());
                        } catch (Exception e) {
                            throw new RuntimeException(e);
                        }
                    }
                    @Override
                    public Key resolveSigningKey(JwsHeader jwsHeader, Claims claims) {
                        return getPublicKey(jwsHeader);
                    }
                    @Override
                    public Key resolveSigningKey(JwsHeader jwsHeader, String s) {
                        return getPublicKey(jwsHeader);
                    }
                };
                // Verify and parse the message content.
                JwtParser parser = Jwts.parserBuilder()
                        .requireIssuer(issuer)
                        .requireAudience(clientId)
                        .setAllowedClockSkewSeconds(60)
                        .setSigningKeyResolver(signingKeyResolver)
                        .build();
                return parser.parse(token);
            } catch (IncorrectClaimException e) {
                // The claim of the message is invalid. Handle the exception (for example, recording logs).
                log.error("claim invalid", e);
            } catch (SignatureException e) {
                // Failed to verify the signature. Handle the exception (for example, recording logs).
                log.error("verify signature failed", e);
            } catch (Exception e) {
                // For other exceptions, handle them according to your own service needs.
                log.error("valid event token failed", e);
            }
            return null;
        }
    
        private PublicConfiguration getPublicConfiguration() {
            PublicConfiguration publicConfiguration = this.publicConfigurationCache.get("DEFAULT");
            if (publicConfiguration == null) {
                throw new IllegalArgumentException("public configuration get failed!");
            }
            return publicConfiguration;
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
    
        @Data
        static class PublicConfiguration {
            private String issuer;
            private String jwksUri;
        }
    }
    
2.  **Process the message body.**
    
    -   **Message body in JSON object format**
        
        Message example: A user deregisters a HUAWEI ID.
        
        {
          "iss": "id.cloud.huawei.com",
          "aud": "<_Client ID_\>",
          "iat": 1727619834,
          "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
          "events": {
            "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
              "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                "subject\_type": "iss\_sub"
              }
            }
          }
        }
        
        Message example: A user revokes authorization on an app.
        
        {
          "iss": "id.cloud.huawei.com",
          "aud": "<_Client ID_\>",
          "iat": 1750403661,
          "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
          "events": {
            "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
              "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                "subject\_type": "iss\_sub"
              },
              "scopes": \[
                "phone",
                "userConsent",
                "openid",
                "email"
              \]
            }
          }
        }
        
        Message example: A user changes their authorized mobile number.
        
        {
          "iss": "id.cloud.huawei.com",
          "aud": "<_Client ID_\>",
          "iat": 1750385669,
          "jti": "c27c197ba5c94081aa32b8dbc52389f3",
          "events": {
            "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
              "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                "subject\_type": "iss\_sub"
              }
            }
          }
        }
        
    
    -   **Message body in JSON array format**
        
        Message example: A user deregisters a HUAWEI ID.
        
        \[
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750385669,
            "jti": "6672ed7d5c5e4c3c92f343ecac40f326",
            "events": {
              "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                }
              }
            }
          },
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750385669,
            "jti": "6672ed7d5c5e4c3c92f343ecac40f325",
            "events": {
              "https://schemas.openid.net/secevent/risc/event-type/account-purged": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                }
              }
            }
          }
        \]
        
        Message example: A user revokes authorization on an app.
        
        \[
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750403661,
            "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb56",
            "events": {
              "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                },
                "scopes": \[
                  "phone",
                  "userConsent",
                  "openid",
                  "email"
                \]
              }
            }
          },
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750403661,
            "jti": "97af1abdbbcd4f00a6d8b74c9b1bbb57",
            "events": {
              "https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                },
                "scopes": \[
                  "phone",
                  "userConsent",
                  "openid",
                  "email"
                \]
              }
            }
          }
        \]
        
        Message example: A user changes their authorized mobile number.
        
        \[
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750385669,
            "jti": "c27c197ba5c94081aa32b8dbc52389f3",
            "events": {
              "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                }
              }
            }
          },
          {
            "iss": "id.cloud.huawei.com",
            "aud": "<_Client ID_\>",
            "iat": 1750385669,
            "jti": "c27c197ba5c94081aa32b8dbc52389f4",
            "events": {
              "https://schemas.openid.net/secevent/oauth/event-type/phone-modified": {
                "subject": {
                "extra": "<_OpenID of the user who triggers an event_\>",
                  "iss": "id.cloud.huawei.com",
                "sub": "<_UnionID of the user who triggers an event_\>",
                  "subject\_type": "iss\_sub"
                }
              }
            }
          }
        \]
        
    
    The parameters in the preceding code are described as follows.
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    aud
    
     | 
    
    Client ID, which is the same as that in [Subscribing to User Information Changes](#section1430414972716).
    
     |
    | 
    
    iss
    
     | 
    
    Message sender identifier. The value is always **id.cloud.huawei.com**.
    
     |
    | 
    
    iat
    
     | 
    
    UTC timestamp (in seconds) when an event is generated.
    
     |
    | 
    
    jti
    
     | 
    
    Unique random character string, which helps you to identify the redelivered message body.
    
     |
    | 
    
    events
    
     | 
    
    User information change event and its message body. The format is JSON. **key** indicates the user information change event type, and **value** indicates the message body of the event.
    
     |
    | 
    
    subject
    
     | 
    
    Message body of the user information change event. The format is JSON. Here are included fields:
    
    -   **sub**: UnionID of the user who triggers an event. (The value is unique for each user across all apps of the same developer.) For details about the format requirements, please refer to [Formats of OpenID and UnionID](../faqs/formats-of-openid-and-unionid/document.md).
    -   **subject\_type**: The value is always **iss\_sub**.
    -   **extra**: OpenID of the user who triggers an event. (The value is unique for each user within the same app.) For details about the format requirements, please refer to [Formats of OpenID and UnionID](../faqs/formats-of-openid-and-unionid/document.md).
    -   **iss**: Message sender identifier. The value is always **id.cloud.huawei.com**.
    
     |
    | 
    
    scopes
    
     | 
    
    Revoked scopes, in the format of a JSON array. This field is available only when the event type is **\[****https://schemas.openid.net/secevent/oauth/event-type/tokens-revoked****\]**.
    
     |
