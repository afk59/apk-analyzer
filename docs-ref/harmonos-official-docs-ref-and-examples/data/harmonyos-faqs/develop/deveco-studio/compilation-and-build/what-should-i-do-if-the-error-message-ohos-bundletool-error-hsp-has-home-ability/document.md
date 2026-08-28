# What should I do if the error message "Ohos BundleTool \[Error\]: hsp has home ability;Ohos BundleTool \[Error\]: CompressEntrance::main exit, verify failed." is displayed during an HSP build?

**Symptom**

During an HSP build, the following error message is displayed: "Ohos BundleTool \[Error\]: hsp has home ability;Ohos BundleTool \[Error\]: CompressEntrance::main exit, verify failed."

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/0nKyqNjLTCOh2pjTs1FS0A/en-us_image_0000002229758781.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38CFA7FB726D66EAA111E8F327D6360F6676A381417381AF8060CBB14A7563D6)

**Possible Causes**

1.  Since DevEco Studio 5.0.2 Beta1, an HSP supports all UIAbility components except the entry ability.
2.  During the build, abilities in the dependent HAR are combined with the HSP configuration. Therefore, an HSP does not support HARs with an entry ability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BRVYuYHCS4WBlSHmqfDbxw/en-us_image_0000002229604285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06AB8EAD2D42C08E29812F867639095E8F6E231A85FACA2832610D7D87D610C8)

**Solution**

1.  Check the **module.json5** file of the HSP and remove any unnecessary **skills** configurations in the entry ability. Then rebuild the module.
2.  Check the **module.json5** file of the HAR on which the HSP depends. If the entry ability in the HAR is configured, do the following:
    1.  If it is a local source dependency, remove the entry ability configuration from the HAR and rebuild the module, or remove the dependency from the HSP.
    2.  If it is a third-party package dependency, remove the entry ability configuration from the HAR and republish the updated version. After updating the version, rebuild the HSP.
    3.  If the third-party HAR cannot be republished, use the Hvigor plugin to add a custom task to delete the entry ability configuration from **build/${productName}/intermediates/package/${targetName}/module.json**, and rebuild the HSP.
        
        // HSP module hvigorfile.ts
        import { hspTasks,OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
        import { hvigor, HvigorNode, HvigorPlugin,FileUtil } from '@ohos/hvigor';
        export function customPlugin():HvigorPlugin {
            return {
                pluginId: 'customPlugin',
                context() {
                    return {
                        data: 'customPlugin xxx'
                    };
                },
                apply(currentNode:HvigorNode): Promise<void> {
                    hvigor.nodesEvaluated(async () => {
                        hspTask(currentNode);
                    });
                }
            }
        }
        function hspTask(currentNode: HvigorNode) {
            // Obtain contextual information of the HSP module
            const hspContext = currentNode.getContext(OhosPluginId.OHOS\_HSP\_PLUGIN) as OhosHspContext;
            hspContext?.targets((target: Target) => {
                const targetName = target.getTargetName();
                const outputPath = target.getBuildTargetOutputPath();
                const task = currentNode.getTaskByName(\`${targetName}@GeneratePkgModuleJson\`);
                currentNode.registerTask({
                    // TASK
                    name: \`${targetName}@changeModuleJson\`,
                    // Task execution logic entity function
                    run() {
                        const moduleJson = FileUtil.readJson5(outputPath+"/../../intermediates/package/"+targetName+"/module.json");
                        const abilities = moduleJson\['module'\]\['abilities'\];
                        abilities.forEach((ability)=>{
                            delete ability\['skills'\];
                        })
                        console.log('begin to rewrite module.json file.');
                        moduleJson\['module'\]\['abilities'\] = abilities
                        FileUtil.writeFileSync(outputPath+"/../../intermediates/package/"+targetName+"/module.json",JSON.stringify(moduleJson));
                    },
                    // Configure prerequisite task dependencies
                    dependencies: \[\`${targetName}@GeneratePkgModuleJson\`\],
                    // Post task dependencies for configuring tasks
                    postDependencies: \[\`${targetName}@PackageSharedHar\`\]
                });
            });
        }
        export default {
            system: hspTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
            plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
        }
