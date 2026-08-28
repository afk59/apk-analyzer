# Rule Changes

#### 6.0.2.636

**New Rules**

-   [@correctness/redundant-dependency-check](../correctness-correctness-rules/correctness-redundant-dependency-check/document.md)
-   [@cross-device-app-dev/immersive-effect-check](../cross-device-app-dev-rules-oriented-to-one-time-development-for-multi-device-dep/cross-device-app-dev-immersive-effect-check/document.md)

#### 6.0.1.246

**New Rules**

-   [@compatibility/api-compatibility-check](../compatibility-compatibility-rules/compatibility-api-compatibility-check/document.md)

#### 6.0.0.848

**New Rules**

-   [@security/no-unsafe-kdf](../security-security-rules/security-no-unsafe-kdf/document.md)
-   [@security/no-unsafe-sm4](../security-security-rules/security-no-unsafe-sm4/document.md)
-   [@security/no-unsafe-sm2-key](../security-security-rules/security-no-unsafe-sm2-key/document.md)
-   [@security/no-unsafe-sm2-cipher](../security-security-rules/security-no-unsafe-sm2-cipher/document.md)
-   [@security/no-unsafe-ecdh](../security-security-rules/security-no-unsafe-ecdh/document.md)
-   [@security/no-unsafe-huks](../security-security-rules/security-no-unsafe-huks/document.md)

#### 6.0.0.828

**New Rules**

-   [@performance/no-use-any-import](../performance-performance-rules/performance-no-use-any-import/document.md)
-   [@performance/avoid-overusing-custom-component-check](../performance-performance-rules/performance-avoid-overusing-custom-component-check/document.md)
-   [@performance/bad-deep-clone-check](../performance-performance-rules/performance-bad-deep-clone-check/document.md)
-   [@performance/reasonable-audio-use-check](../performance-performance-rules/performance-reasonable-audio-use-check/document.md)
-   [@performance/reasonable-sensor-use-check](../performance-performance-rules/performance-reasonable-sensor-use-check/document.md)
-   [@performance/reasonable-gps-use-check](../performance-performance-rules/performance-reasonable-gps-use-check/document.md)
-   [@performance/reuse-date-instances-check](../performance-performance-rules/performance-reuse-date-instances-check/document.md)
-   [@performance/crypto-replacement-check](../performance-performance-rules/performance-crypto-replacement-check/document.md)
-   [@performance/monitor-invisible-area-in-image-animation](../performance-performance-rules/performance-monitor-invisible-area-in-image-animation/document.md)
-   [@performance/datashare-query-unrelease-check](../performance-performance-rules/performance-datashare-query-unrelease-check/document.md)
-   [@performance/dark-color-mode-check](../performance-performance-rules/performance-dark-color-mode-check/document.md)
-   [@performance/update-state-var-between-animatetos-check](../performance-performance-rules/performance-update-state-var-between-animatetos-check/document.md)
-   [@performance/tabs-on-change-check](../performance-performance-rules/performance-tabs-on-change-check/document.md)
-   [@performance/nested-post-frame-callback-check](../performance-performance-rules/performance-nested-post-frame-callback-check/document.md)
-   [@cross-device-app-dev/window-size-change-listener-check](../cross-device-app-dev-rules-oriented-to-one-time-development-for-multi-device-dep/cross-device-app-dev-window-size-change-listener-check/document.md)

#### 6.0.0.418

**New Rules**

-   [@performance/web-on-active-check](../performance-performance-rules/performance-web-on-active-check/document.md)
-   [@performance/gif-hardware-decoding-check](../performance-performance-rules/performance-gif-hardware-decoding-check/document.md)
-   [@cross-device-app-dev/one-multi-breakpoint-check](../cross-device-app-dev-rules-oriented-to-one-time-development-for-multi-device-dep/cross-device-app-dev-one-multi-breakpoint-check/document.md)

Changed rules

-   [@typescript-eslint/explicit-function-return-type](../typescript-eslint-general-rules/typescript-eslint-explicit-function-return-type/document.md): option **allowArkTS** added. The default value is **false**. If this option is set to **true**, the .ets file can be checked.

#### 5.1.0.828

**New Rules**

-   [@performance/web-cache-mode-check](../performance-performance-rules/performance-web-cache-mode-check/document.md)
-   [@correctness/audio-interrupt-check](../correctness-correctness-rules/correctness-audio-interrupt-check/document.md)
-   [@correctness/audio-pause-or-mute-check](../correctness-correctness-rules/correctness-audio-pause-or-mute-check/document.md)
-   [@correctness/avsession-metadata-check](../correctness-correctness-rules/correctness-avsession-metadata-check/document.md)
-   [@correctness/avsession-buttons-check](../correctness-correctness-rules/correctness-avsession-buttons-check/document.md)
-   [@correctness/image-interpolation-check](../correctness-correctness-rules/correctness-image-interpolation-check/document.md)
-   [@correctness/image-pixel-format-check](../correctness-correctness-rules/correctness-image-pixel-format-check/document.md)
-   [@performance/hp-ffrt-no-use-std](../performance-performance-rules/performance-hp-ffrt-no-use-std/document.md)

Changed rules

-   [@performance/hp-arkui-use-taskpool-for-web-request](../performance-performance-rules/performance-hp-arkui-use-taskpool-for-web-request/document.md): moved from the **recommended** rule set to the **all** rule set.

#### 5.0.7.100

**New Rules**

-   [@performance/foreach-index-check](../performance-performance-rules/performance-foreach-index-check/document.md)
-   [@performance/js-code-cache-by-precompile-check](../performance-performance-rules/performance-js-code-cache-by-precompile-check/document.md)
-   [@performance/js-code-cache-by-interception-check](../performance-performance-rules/performance-js-code-cache-by-interception-check/document.md)
-   [@performance/init-list-component](../performance-performance-rules/performance-init-list-component/document.md)
-   [@correctness/listen-default-network-change](../correctness-correctness-rules/correctness-listen-default-network-change/document.md)
-   [@correctness/listen-multi-network-concurrent](../correctness-correctness-rules/correctness-listen-multi-network-concurrent/document.md)
-   [@security/no-unsafe-3des](../security-security-rules/security-no-unsafe-3des/document.md)

**Changed Rules**

-   [@performance/high-frequency-log-check](../performance-performance-rules/performance-high-frequency-log-check/document.md): adds a check on the frequently called function **onWillScroll**.
-   [@typescript-eslint/prefer-readonly-parameter-types](../typescript-eslint-general-rules/typescript-eslint-prefer-readonly-parameter-types/document.md) and [@typescript-eslint/no-magic-numbers](../typescript-eslint-general-rules/typescript-eslint-no-magic-numbers/document.md): changes the default severity from error to warn.
-   [@typescript-eslint/lines-between-class-members](../typescript-eslint-general-rules/typescript-eslint-lines-between-class-members/document.md): updated from requiring blank lines between member variables to no longer requiring blank lines between member variables.
-   [@security/no-unsafe-hash](../security-security-rules/security-no-unsafe-hash/document.md): adds checks for insecure hash algorithms in the @ohos/crypto-js package.
-   [@security/no-unsafe-mac](../security-security-rules/security-no-unsafe-mac/document.md): adds checks for insecure MAC algorithms in the @ohos/crypto-js package.

#### 5.0.5.200

**Changed Rules**

-   [@performance/hp-arkui-avoid-empty-callback](../performance-performance-rules/performance-hp-arkui-avoid-empty-callback/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](../performance-performance-rules/performance-hp-arkui-use-word-break-to-replace-zero-width-space/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/hp-arkui-remove-redundant-nest-container](../performance-performance-rules/performance-hp-arkui-remove-redundant-nest-container/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/hp-arkui-remove-container-without-property](../performance-performance-rules/performance-hp-arkui-remove-container-without-property/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/sparse-array-check](../performance-performance-rules/performance-sparse-array-check/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/number-init-check](../performance-performance-rules/performance-number-init-check/document.md): moved from the **Recommended** plan to the **All** plan.
-   [@performance/typed-array-check](../performance-performance-rules/performance-typed-array-check/document.md): moved from the **Recommended** plan to the **All** plan.

#### 5.0.3.800

**New Rules**

-   [@performance/hp-arkui-reduce-pangesture-distance](../performance-performance-rules/performance-hp-arkui-reduce-pangesture-distance/document.md)
-   [@performance/hp-arkui-suggest-use-get-anonymousid-async](../performance-performance-rules/performance-hp-arkui-suggest-use-get-anonymousid-async/document.md)
-   [@performance/multiple-associations-state-var-check](../performance-performance-rules/performance-multiple-associations-state-var-check/document.md)
-   [@performance/constant-property-referencing-check-in-loops](../performance-performance-rules/performance-constant-property-referencing-check-in-loops/document.md)
-   [@performance/foreach-args-check](../performance-performance-rules/performance-foreach-args-check/document.md)

**Changed Rules**

-   [@security/specified-interface-call-chain-check](../security-security-rules/security-specified-interface-call-chain-check/document.md): adds namespace, type, interface, enum, and struct support; changes the configuration type of the **namespace** field from string to array.

-   [@performance/high-frequency-log-check](../performance-performance-rules/performance-high-frequency-log-check/document.md): changes the default severity from suggestion to warn; added to the **All** plan.
-   [@performance/number-init-check](../performance-performance-rules/performance-number-init-check/document.md): changes the default severity from warn to suggestion; added to the **Recommended** plan.
-   [@performance/start-window-icon-check](../performance-performance-rules/performance-start-window-icon-check/document.md): changes the default severity from warn to suggestion; added to the **Recommended** plan.
-   [@performance/sparse-array-check](../performance-performance-rules/performance-sparse-array-check/document.md): changes the default severity from warn to suggestion; added to the **Recommended** plan.
-   [@performance/typed-array-check](../performance-performance-rules/performance-typed-array-check/document.md): changes the default severity from warn to suggestion; added to the **Recommended** plan.
-   [@performance/waterflow-data-preload-check](../performance-performance-rules/performance-waterflow-data-preload-check/document.md): added to the **Recommended** plan.
-   [@performance/hp-arkts-no-use-any-export-current](../performance-performance-rules/performance-hp-arkts-no-use-any-export-current/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkts-no-use-any-export-other](../performance-performance-rules/performance-hp-arkts-no-use-any-export-other/document.md): added to the **Recommended** plan.
-   [@performance/hp-arkui-avoid-empty-callback](../performance-performance-rules/performance-hp-arkui-avoid-empty-callback/document.md): changes the severity from warn to suggestion.
-   [@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse](../performance-performance-rules/performance-hp-arkui-avoid-update-auto-state-var-in-abouttoreuse/document.md): added to the **Recommended** rule set.
-   [@performance/hp-arkui-image-async-load](../performance-performance-rules/performance-hp-arkui-image-async-load/document.md): moved from the **recommended** rule set to the **all** rule set.
-   [@performance/hp-arkui-load-on-demand](../performance-performance-rules/performance-hp-arkui-load-on-demand/document.md): changes the severity from suggestion to warn.
-   [@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator](../performance-performance-rules/performance-hp-arkui-no-stringify-in-lazyforeach-key-generator/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-remove-container-without-property](../performance-performance-rules/performance-hp-arkui-remove-container-without-property/document.md): changes the severity from warn to suggestion.
-   [@performance/hp-arkui-remove-redundant-nest-container](../performance-performance-rules/performance-hp-arkui-remove-redundant-nest-container/document.md): changes the severity from warn to suggestion.
-   [@performance/hp-arkui-replace-nested-reusable-component-by-builder](../performance-performance-rules/performance-hp-arkui-replace-nested-reusable-component-by-builder/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-suggest-cache-avplayer](../performance-performance-rules/performance-hp-arkui-suggest-cache-avplayer/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component](../performance-performance-rules/performance-hp-arkui-suggest-reuseid-for-if-else-reusable-component/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-suggest-use-effectkit-blur](../performance-performance-rules/performance-hp-arkui-suggest-use-effectkit-blur/document.md): added to the **Recommended** plan.
-   [@performance/hp-arkui-use-grid-layout-options](../performance-performance-rules/performance-hp-arkui-use-grid-layout-options/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-use-local-var-to-replace-state-var](../performance-performance-rules/performance-hp-arkui-use-local-var-to-replace-state-var/document.md): changes the severity from suggestion to warn.
-   [@performance/hp-arkui-use-onAnimationStart-for-swiper-preload](../performance-performance-rules/performance-hp-arkui-use-onanimationstart-for-swiper-preload/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-use-reusable-component](../performance-performance-rules/performance-hp-arkui-use-reusable-component/document.md): changes the severity from suggestion to warn.
-   [@performance/hp-arkui-use-row-column-to-replace-flex](../performance-performance-rules/performance-hp-arkui-use-row-column-to-replace-flex/document.md): moved from the **recommended** rule set to the **all** rule set.
-   [@performance/hp-arkui-use-scale-to-replace-attr-animateto](../performance-performance-rules/performance-hp-arkui-use-scale-to-replace-attr-animateto/document.md): changes the severity from suggestion to warn; added to the **Recommended** rule set.
-   [@performance/hp-arkui-use-taskpool-for-web-request](../performance-performance-rules/performance-hp-arkui-use-taskpool-for-web-request/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-use-transition-to-replace-animateto](../performance-performance-rules/performance-hp-arkui-use-transition-to-replace-animateto/document.md): changes the severity from suggestion to warn; added to the **Recommended** plan.
-   [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](../performance-performance-rules/performance-hp-arkui-use-word-break-to-replace-zero-width-space/document.md): added to the **Recommended** plan.
-   [@performance/hp-arkui-set-cache-count-for-lazyforeach-grid](../performance-performance-rules/performance-hp-arkui-set-cache-count-for-lazyforeach-grid/document.md): changes the severity from warn to suggestion.
    

**Removed Rules**

-   [@performance/hp-arkui-wrap-waterflow-if-else-footer](../performance-performance-rules/performance-hp-arkui-wrap-waterflow-if-else-footer-deprecated/document.md)

#### 5.0.3.600

**New Rules**

-   [@performance/hp-arkui-wrap-waterflow-if-else-footer](../performance-performance-rules/performance-hp-arkui-wrap-waterflow-if-else-footer-deprecated/document.md)
-   [@performance/hp-arkui-remove-unchanged-state-var](../performance-performance-rules/performance-hp-arkui-remove-unchanged-state-var/document.md)
-   [@performance/hp-arkts-no-use-any-export-current](../performance-performance-rules/performance-hp-arkts-no-use-any-export-current/document.md)
-   [@performance/hp-arkts-no-use-any-export-other](../performance-performance-rules/performance-hp-arkts-no-use-any-export-other/document.md)
-   [@performance/hp-arkui-suggest-cache-avplayer](../performance-performance-rules/performance-hp-arkui-suggest-cache-avplayer/document.md)
-   [@performance/hp-arkui-suggest-use-effectkit-blur](../performance-performance-rules/performance-hp-arkui-suggest-use-effectkit-blur/document.md)
-   [@performance/lottie-animation-destroy-check](../performance-performance-rules/performance-lottie-animation-destroy-check/document.md)
-   [@performance/timezone-interface-check](../performance-performance-rules/performance-timezone-interface-check/document.md)

**Changed Rules**

For certain scenarios of the following rules, Code Linter checks report errors after DevEco Studio is upgraded to 5.0.3.600, which do not occur in previous versions.

-   [@typescript-eslint/no-unnecessary-condition](../typescript-eslint-general-rules/typescript-eslint-no-unnecessary-condition/document.md)

// Scenario 1: logical expression check
interface GeneratedTypeLiteralInterface {}
declare let foo: GeneratedTypeLiteralInterface;
foo ??= 1; // This does not trigger an error before the upgrade, but it will after the upgrade.
// Scenario 2: In chain expressions where non-nullity can be inferred, there is no need to add null checks.
interface GeneratedTypeLiteralInterface {
  bar: () => number;
}
type Foo = GeneratedTypeLiteralInterface | null;
declare const foo: Foo;
foo?.bar()?.toExponential(); // This does not trigger an error before the upgrade, but it will after the upgrade.

-   [@typescript-eslint/promise-function-async](../typescript-eslint-general-rules/typescript-eslint-promise-function-async/document.md)

// In scenarios where a function's return type is not explicitly defined and the return value could be a Promise, the function should be defined as async.
function promiseInUnionWithoutExplicitReturnType(p: boolean) { // This does not trigger an error before the upgrade, but it will after the upgrade.
  return p ? Promise.resolve(5) : 5;
}

-   [@typescript-eslint/member-ordering](../typescript-eslint-general-rules/typescript-eslint-member-ordering/document.md)

// When the optionalityOrder option is configured and the class property does not contain optional variables, the order option configured in the rule is ineffective in previous versions.
// Rule settings: "@typescript-eslint/member-ordering": \["error", {"default": {"memberTypes": 'never', "order": 'natural-case-insensitive', "optionalityOrder": 'required-first',}}\].
class X {
  b: string = '';
  a: string = ''; // This does not trigger an error before the upgrade, but it will after the upgrade.
}

-   [@typescript-eslint/naming-convention](../typescript-eslint-general-rules/typescript-eslint-naming-convention/document.md)

// Support for checking typeMethod in the interface
// Rule settings: "@typescript-eslint/naming-convention": \["error", {selector: 'typeMethod', format: \['PascalCase'\]}\].
interface SOME\_INTERFACE {
  someMethod: () => void; // This does not trigger an error before the upgrade, but it will after the upgrade.
  some\_property: string;
}

-   [@typescript-eslint/ban-types](../typescript-eslint-general-rules/typescript-eslint-ban-types/document.md)

// Support for checking the type after extend and implements
// Rule settings: "@typescript-eslint/ban-types": \["error",{"types": {"Bar": {"message": ""}}}\].
interface Bar {}
interface Baz {}
interface Foo extends Bar, Baz {} // This does not trigger an error before the upgrade, but it will after the upgrade.

-   [@typescript-eslint/no-floating-promises](../typescript-eslint-general-rules/typescript-eslint-no-floating-promises/document.md)

// Scenario 1: .finally() is considered as not effectively handling potential exceptions that may occur in the Promise.
Promise.reject().finally(() => {}) // This does not trigger an error before the upgrade, but it will after the upgrade.
// Scenario 2: If the second parameter in .then() is undefined or null, it is considered as not effectively handling potential exceptions that may occur in the Promise.
Promise.resolve().then(() => {}, undefined); // This does not trigger an error before the upgrade, but it will after the upgrade.
Promise.resolve().then(() => {}, null); // This does not trigger an error before the upgrade, but it will after the upgrade.

-   [@typescript-eslint/no-inferrable-types](../typescript-eslint-general-rules/typescript-eslint-no-inferrable-types/document.md)

// Support for checking the parameter type in the constructor
class Foo {
  constructor(param: boolean = true) {} // This does not trigger an error before the upgrade, but it will after the upgrade.
}

-   [@typescript-eslint/prefer-readonly](../typescript-eslint-general-rules/typescript-eslint-prefer-readonly/document.md)

interface GeneratedObjectLiteralInterface {
  prop?: string
}

class Test {
// Support for checking private properties
  #testObj: GeneratedObjectLiteralInterface = {}; // This does not trigger an error before the upgrade, but it will after the upgrade.

  public test(): void {
    this.#testObj?.prop;
  }
}

#### 5.0.3.500

**New Rules**

-   [@security/no-unsafe-dh-key](../security-security-rules/security-no-unsafe-dh-key/document.md)
-   [@security/no-unsafe-dsa-key](../security-security-rules/security-no-unsafe-dsa-key/document.md)
-   [@security/no-unsafe-rsa-key](../security-security-rules/security-no-unsafe-rsa-key/document.md)
-   [@performance/hp-arkui-use-attributeUpdater-control-refresh-scope](../performance-performance-rules/performance-hp-arkui-use-attributeupdater-control-refresh-scope/document.md)
-   [@performance/hp-arkui-use-id-in-get-resource-sync-api](../performance-performance-rules/performance-hp-arkui-use-id-in-get-resource-sync-api/document.md)
-   [@performance/hp-arkui-use-transition-to-replace-animateto](../performance-performance-rules/performance-hp-arkui-use-transition-to-replace-animateto/document.md)
-   [@performance/hp-arkui-remove-redundant-state-var](../performance-performance-rules/performance-hp-arkui-remove-redundant-state-var/document.md)
-   [@performance/hp-arkui-use-taskpool-for-web-request](../performance-performance-rules/performance-hp-arkui-use-taskpool-for-web-request/document.md)
-   [@security/specified-interface-call-chain-check](../security-security-rules/security-specified-interface-call-chain-check/document.md)
-   [@hw-stylistic/file-naming-convention](../hw-stylistic-arkts-code-style-rules/hw-stylistic-file-naming-convention/document.md)

**Changed Rules**

-   @performance/high-frequency-log-check: moved from the **All** plan to the **Recommended** plan.

**Removed Rules**

-   [@performance/object-creation-check](../performance-performance-rules/performance-object-creation-check-deprecated/document.md)
-   [@performance/hp-arkui-limit-refresh-scope](../performance-performance-rules/performance-hp-arkui-limit-refresh-scope-deprecated/document.md)
-   [@performance/lazyforeach-args-check](../performance-performance-rules/performance-lazyforeach-args-check-deprecated/document.md)
