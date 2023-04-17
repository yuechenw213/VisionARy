using System.Collections;
using System.Collections.Generic;

using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(LoadPointCloudScript))]
public class LoadPointCloudScriptEditor : Editor
{
    private SerializedProperty pointSizeField;
    private SerializedProperty fileField;
    private SerializedProperty folderField;

    private void OnEnable()
    {
        pointSizeField = serializedObject.FindProperty("pointSize");
        fileField = serializedObject.FindProperty("filePath");
        folderField = serializedObject.FindProperty("folderPath");
    }

    public override void OnInspectorGUI()
    {

        serializedObject.Update();
        EditorGUILayout.PropertyField(pointSizeField);
        // Display the fields and buttons in the desired order
        EditorGUILayout.PropertyField(fileField);
        if (GUILayout.Button("Load Point Cloud"))
        {
            // Load the mesh from the file and set it for the mesh filter component
            ((LoadPointCloudScript)target).StartLoad();
        }

        EditorGUILayout.PropertyField(folderField);
        if (GUILayout.Button("Load All Point Cloud"))
        {
            // Load the mesh from the file and set it for the mesh filter component
            ((LoadPointCloudScript)target).StartLoadFolder();
        }

        serializedObject.ApplyModifiedProperties();

    }
}
